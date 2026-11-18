"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _facts(ctx, action):
    """Nguồn sự thật cho lệnh ghi: kiện của ticket, độ trễ theo tracking DB, chính sách hiệu lực. Không đọc chữ khách."""
    order = ctx.tools.lookup_order(action.get("order_id") or ctx.ticket.get("order_id"))
    if not order:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return None
    return order, parcel, delay, policy


def pre_guard(ctx):
    # Cổng 1 (pre-mortem "chính sách đổi mà agent đọc cờ index cũ"): ghim chính sách theo NGÀY HIỆU LỰC, không theo cờ.
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is not None:
        return Verdict.allow(policy_id=policy["policy_id"])
    return Verdict.escalate("không có chính sách hiệu lực hôm nay")


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    limits = ctx.tools.ops_limits()

    if tool == "issue_refund":
        # Cổng 2: tiền chỉ theo quyền lợi tính từ tracking DB (không theo số ngày khách khai, không theo lời "hoàn đầy đủ").
        if action.get("payer", "LOGIX") != "LOGIX":
            return Verdict.escalate("hoàn tiền trừ vào tài khoản shop (MERCHANT) phải có người duyệt")
        f = _facts(ctx, action)
        if f is None:
            return Verdict.escalate("thiếu dữ liệu đơn hoặc chính sách để kiểm tiền hoàn")
        order, parcel, delay, policy = f
        cause = parcel.get("delay_cause") or ("CARRIER" if delay > 0 else None)
        ent = H.entitlement_vnd(policy, order, delay, cause)
        already = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=action["order_id"]))  # chặn hoàn trùng / ghi lặp
        remaining = ent - already
        amount = action.get("amount_vnd", 0)
        if remaining <= 0:
            ctx.log("refund_blocked_no_entitlement", entitlement=ent, already=already, asked=amount)
            return Verdict.deny("không còn quyền lợi hoàn theo tracking DB hoặc đã hoàn rồi")
        approved = False
        if action.get("approval_id"):
            ap = next(iter(ctx.tools.lookup_approvals(approval_id=action["approval_id"])), None)
            approved = bool(ap and ap["status"] == "valid" and ap["expires_at"] >= ctx.as_of
                            and ap["order_id"] == action["order_id"] and ap["max_vnd"] >= min(amount, remaining))
            if not approved:
                return Verdict.escalate("phê duyệt không hợp lệ (hết hạn, đã dùng, sai đơn hoặc không đủ hạn mức)")
        if not approved:
            if min(amount, remaining) > policy["auto_limit_vnd"]:
                return Verdict.escalate("vượt hạn mức tự động của chính sách, cần người duyệt")
            today = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(customer_id=ctx.ticket.get("customer_id"))
                        if not r.get("approval_id"))
            if today + min(amount, remaining) > limits.get("max_auto_refund_per_customer_per_day_vnd", 10 ** 9):
                return Verdict.escalate("tổng hoàn tự động cho một khách vượt trần ngày")
            if H.carrier_at_fault(policy, parcel, delay):   # lỗi hãng sắp ghi là lỗi thứ 3 trong ngày → chuyển người TRƯỚC khi hoàn
                strikes = len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"]))
                if strikes >= limits.get("max_auto_strikes_per_carrier_per_day", 2):
                    return Verdict.escalate("hãng đã có 2 lỗi tự động trong ngày, lỗi thứ 3 cần người duyệt")
        if amount > remaining:
            ctx.log("refund_capped_to_entitlement", asked=amount, entitlement=remaining)
            return Verdict.modify("giảm tiền hoàn về quyền lợi theo tracking DB", amount_vnd=remaining)
        return Verdict.allow()

    if tool == "file_carrier_fault":
        # Cổng 3: lỗi hãng chỉ khi tracking ghi nguyên nhân hợp lệ và trễ đủ ngày; hãng/kiện lấy từ DB.
        f = _facts(ctx, action)
        if f is None:
            return Verdict.deny("thiếu dữ liệu để xác nhận lỗi hãng")
        order, parcel, delay, policy = f
        if not H.carrier_at_fault(policy, parcel, delay):
            ctx.log("fault_blocked", delay=delay, cause=parcel.get("delay_cause"))
            return Verdict.deny("tracking DB không đủ điều kiện ghi lỗi hãng (trễ chưa đủ ngày hoặc nguyên nhân không thuộc lỗi hãng)")
        if len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= limits.get("max_auto_strikes_per_carrier_per_day", 2):
            return Verdict.escalate("hãng đã có 2 lỗi tự động trong ngày, lỗi thứ 3 cần người duyệt")
        return Verdict.modify("ghi đúng hãng, kiện, số ngày theo tracking DB", carrier_id=parcel["carrier_id"],
                              parcel_id=parcel["parcel_id"], driver_id=parcel.get("driver_id"), delay_days=delay)

    if tool == "notify_carrier":
        # Cổng 4: chỉ gửi hãng đúng các trường chính sách cho phép; chữ khách và thông tin người nhận không rời LogiX.
        f = _facts(ctx, action)
        if f is None:
            return Verdict.deny("thiếu chính sách để biết trường được phép gửi hãng")
        _, parcel, delay, policy = f
        allowed = set(policy["carrier_notice_fields"])
        payload = {k: v for k, v in (action.get("payload") or {}).items() if k in allowed}
        if "delay_days" in payload:
            payload["delay_days"] = delay
        if payload != action.get("payload"):
            ctx.log("notice_filtered", dropped=sorted(set(action.get("payload") or {}) - allowed))
            return Verdict.modify("chỉ gửi hãng các trường chính sách cho phép", payload=payload)

    return Verdict.allow()
