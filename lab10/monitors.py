"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def escalated_llm_cost_avg_vnd(trials):
    """Tiền máy (LLM + nền tảng) trung bình đã tốn cho mỗi ticket rồi vẫn phải chuyển người: tiền máy vô ích.
    Không dùng nhãn; đọc status và cost_vnd của trial."""
    c = [t["cost_vnd"] for t in trials if t["status"] == "escalated"]
    return round(sum(c) / len(c), 1) if c else 0.0


def warehouse_escalation_rate_max(trials):
    """Tỉ lệ chuyển người của kho tệ nhất (kho có ít nhất 5 lần chạy). Kho gần 1.0 nghĩa là tự động hoá ở kho đó chỉ
    thêm tiền máy mà không bớt được công người."""
    by = {}
    for t in trials:
        if t["warehouse"]:                      # đơn không tra được kho không tính vào kho nào
            by.setdefault(t["warehouse"], []).append(t["status"] == "escalated")
    r = [sum(v) / len(v) for v in by.values() if len(v) >= 5]
    return round(max(r), 4) if r else 0.0


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "escalated_llm_cost_avg_vnd": escalated_llm_cost_avg_vnd,
    "warehouse_escalation_rate_max": warehouse_escalation_rate_max,
}
STARTER_MONITORS = ("escalation_rate",)
