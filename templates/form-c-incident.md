# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3A-DAY10-quavuihaha-PoCtoPilotGate1 · **Thẻ đã bốc:** S5 *(đã ghi khớp sổ thẻ S5; lệnh tự kiểm tra đối chiếu dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `<chạy python3 -m lab10.grade --incident S5 lấy mã R-S5-prepared-...>` | S5 · prepared | nhận thẻ đã bốc `S5`, chưa sửa thêm (đúng cổng vòng 1 đã chốt `1b8aeb58`) | 1,0 | 1,0 | 0đ · 0 · 0 | 0,5000 | Cổng vòng 1 chặn hết `890.000đ` hoàn sai và chặn trần LLM (`665đ <= 1.500đ`), nhưng kho `HCM-B2B` vẫn tốn `10.382đ/ticket > 10.000đ` làm tay (`ROI = 0,33`). |
| 2 | `<chạy lab10.eval --suite S5 --stage after>` | S5 · after | thu hẹp `business.pilot_scope` loại kho sỉ `HCM-B2B` (giữ `HN, HCM, DN, CT`, độ phủ `0,6`) + hạ `cost_budget_per_ticket_vnd = 1100` | 1,0 | 1,0 | 0đ · 0 · 0 | 0,1667 | Hết hoàn toàn dòng vượt trần; cắt được kho sỉ lỗ vốn và không ticket lẻ nào vượt trần LLM `1.500đ`. |
| 3 | `<chạy python3 -m lab10.grade --incident S5 lấy mã R-S5-after-...>` | S5 · after | giảm `operations.reviewers_on_shift` từ `2` xuống `1` (`6 ca/giờ`) sau khi đã cắt kho `HCM-B2B` + thêm monitor mới | 1,0 | 1,0 | 0đ · 0 · 0 | 0,1667 | Chi phí còn `3.897đ/ticket`, `ROI = 1,57`, chờ tối đa `0,0 phút`, `0` ca ùn, tiết kiệm ròng `109.857đ/ngày`. |
| 4 | `<chạy lab10.eval --suite base --stage after>` | base · after | (kiểm không regression sau sửa Vòng 2) | 1,0 | 1,0 | 0đ · 0 · 0 | 0,2273 | Không có ca mới hỏng (`newly_failed: []`), chi phí `4.202đ/ticket`, `ROI = 1,38`, hết vượt trần. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `<điền mã R-S5-grade-... khi chạy lab10.grade --incident S5>` · base: `<R-S5-before-...>` · prepared: `<R-S5-prepared-...>`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): Ở mốc `base` (chưa cổng), `S5` chỉ đạt `pass_rate = 0,8333` (`125/150` lần chạy), hoàn sai `890.000đ` (`178.000đ/ngày`), `20` lỗi hãng oan, ticket tốn LLM tới `2.412đ` (> trần `1.500đ`), `ROI = -0,33` (lỗ ròng `-60.486đ/ngày`). Cổng vòng 1 (`prepared`, hash `1b8aeb58`) đã chặn sạch toàn bộ `890.000đ` hoàn sai/trùng, kéo `pass_rate` lên `1,0` (`150/150`), giảm `llm_cost_max` từ `2.412đ` xuống `665đ` (nhờ đặt `cost_budget_per_ticket_vnd = 1500`), đưa `ROI` từ `-0,33` lên `+0,33`.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: Còn **1 dòng vượt trần** ở mốc `prepared`: `! kho HCM-B2B: mỗi ticket tốn 10.382đ > làm tay 10.000đ` (12/12 ticket kho sỉ `O-2550..O-2561` có `review_rate = 1,0`, trợ lý đọc xong đều phải chuyển người duyệt). Ngoài ra chi phí chung toàn bộ vẫn bị kéo lên `7.491đ/ticket` (`ROI = 0,33`) do dư người trực (`reviewers_on_shift = 2`) và gánh kho sỉ.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Chủ yếu thuộc lăng kính **Kinh doanh** (nhóm ticket kho sỉ `HCM-B2B` tự động hoá không thể có lời, chi phí LLM email dài vượt trần `1.500đ`, dư chi phí giữ chỗ người trực) và **Kỹ thuật** (dữ liệu `refund_status` cập nhật batch đêm làm hoàn trùng/lố trên các đơn đã có trong `ledger_seed`).
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? **(1) Đã nằm trong B6:** hai ý về "hoàn trùng khi ghi lặp" (Kỹ thuật) và "một kho tốn nhiều công hơn tiết kiệm / ngân sách" (Kinh doanh) đã có trong B6 — nhờ đó mốc `prepared` đã đỡ được toàn bộ `890.000đ` hoàn trùng/lố (`0đ` ở prepared) và chặn được các email dài `2.412đ` bằng `cost_budget_per_ticket_vnd = 1500`. **(2) Phần bàn chưa nghĩ tới ở vòng 1:** vòng 1 mới nhận diện kho `"?"` đắt hơn làm tay mà chưa soi trước cấu trúc đơn sỉ `HCM-B2B` (`goods_value_vnd >= 2.200.000đ`, quyền lợi `>= 230.000đ > auto_limit_vnd 200.000đ`) khiến 100% đơn kho sỉ luôn tốn cả tiền AI lẫn `10.000đ` công người (`10.382đ > 10.000đ`), và chưa tính rằng đặt `cost_budget_per_ticket_vnd = 1500` sẽ khiến các email hơi dài vẫn lọt qua ngưỡng `read_cost` rồi cộng thêm `300đ` (`policy_check + confirm`) thành vượt trần `1.500đ`.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Đội đã đưa cả kho sỉ `HCM-B2B` (nơi mọi đơn đều `>= 2,2 triệu`, quyền lợi luôn vượt hạn mức tự động `200.000đ` nên `100%` phải chuyển người) vào phạm vi tự động, làm mất cả tiền LLM lẫn `10.000đ` công người duyệt (`10.382đ > 10.000đ` làm tay) | Kinh doanh | `incidents/S5/world_patch.json` (`warehouse_id: HCM-B2B`, `goods_value_vnd: 2.2M–3.4M`), khối `theo kho` trong report `S5` và `config/operating_gates.json -> business.pilot_scope` |
| Đặt ngưỡng ngân sách đọc ticket `cost_budget_per_ticket_vnd = 1500` bằng đúng trần tổng tiền LLM `1.500đ`, bỏ quên khoản `300đ` (`200đ policy_check + 100đ confirm`) phát sinh sau bước đọc nên ticket có độ dài trung bình-cao vẫn có nguy cơ vượt trần `1.500đ` | Kinh doanh & Kỹ thuật | `agent.py` dòng 49–54 & 141–186, `data/world.json -> ops_facts.llm_cost` (`200 + 150 + len//4 + 200 + 100`) |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho `LogiX-VN (ngân sách Finance, chi phí vận hành theo kho và sổ đối soát của chị Oanh NV-OANH)` · đo bằng `wrongful_refund_vnd, cost_per_ticket_vnd theo kho, llm_cost_max_per_ticket_vnd, ROI` · bao nhiêu ở mốc base `hoàn sai 890.000đ (178.000đ/ngày), ticket tốn LLM nhất 2.412đ (> trần 1.500đ), kho HCM-B2B tốn 11.326đ/ticket (> 10.000đ làm tay), lỗ ròng -60.486đ/ngày (ROI -0,33)`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S5-02@11` (`O-2501`), `S5-20@11` (`O-2520`), `S5-21@11` (`O-2521`): khách nhắn lại đa kênh hoặc CSKH đã hoàn tay trước đó (`T-CSKH-2520` hoàn `20.000đ`, `T-CSKH-2521` hoàn `10.000đ` trong `ledger_seed`), nhưng `refund_status` vẫn là `"NONE"` nên trợ lý hoàn tiếp lần 2 (`25.000đ`, `20.000đ`, và `22.000đ` thay vì phần còn thiếu `12.000đ`) + ghi thêm lỗi hãng | Khách không khiếu nại; LogiX mất tiền (`890.000đ` / 5 seed) và chị Oanh (`NV-OANH`) lệch sổ đối soát; hãng vận chuyển (`GHSH`, `VNX`, `MKD`) nhận `20` lỗi oan | cao | **lỗi chìm** |
| 2 | `S5-51@11` (`O-2551`, kho `HCM-B2B`): `goods_value_vnd = 2.350.000đ`, trễ 8 ngày → quyền lợi `230.000đ > auto_limit_vnd 200.000đ`, không có mã duyệt → kết thúc `status=escalated`, tốn `565đ` tiền LLM rồi vẫn phải tốn `10.000đ` công người duyệt (`12/12` đơn kho `HCM-B2B` đều tốn `10.382đ`–`11.326đ/ticket > 10.000đ` làm tay) | CFO & bộ phận Kinh doanh/Vận hành chịu lỗ chi phí trên toàn bộ kho `HCM-B2B` | cao | **giới hạn của hệ thống** |
| 3 | `S5-54@11` (`O-2554`), `S5-50@11` (`O-2550`), `S5-70@11` (`O-2570`): khách kênh `email` dán kèm bảng kê 55–75 dòng mã hàng `SP-xxxx` làm `read_cost` tăng theo độ dài chữ (`1đ / 4 ký tự`), khiến `result.cost_vnd = 2.412đ` (`S5-54@11`) và `2.018đ` (`S5-70@11`), vượt trần `1.500đ/ticket` của Ops | CFO & Quản lý hạ tầng/vận hành chịu chi phí LLM bất thường | cao | **giới hạn của hệ thống** (và **lỗi ngữ cảnh** với khách kho lẻ `S5-70` bị đẩy sang người nếu quá dài) |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | Không | Không | **Đúng:** hệ thống đọc nguyên văn cả phần phụ lục/bảng kê dài hàng nghìn ký tự do khách dán vào email để trích xuất (`read_cost`) mà không cắt bớt hoặc kiểm tra ngân sách ký tự trước. |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | **Đúng:** ở `agent.py` dòng 108, trợ lý chỉ đọc cờ `refund_status` cập nhật theo batch đêm (thiếu dữ liệu giao dịch đã hoàn trong ngày). | **Đúng:** hệ thống không xét ngưỡng `goods_value_vnd` / `warehouse_id = "HCM-B2B"` ở đầu vào nên không biết đơn sỉ chắc chắn vượt hạn mức tự động `200.000đ`. | Không (nhiễu do phụ lục bảng kê dư thừa kèm trong ticket). |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | **Đúng:** CSKH hoàn tay (`T-CSKH-2520`, `T-CSKH-2521` ở `ledger_seed`) và trợ lý cùng ghi sổ cái mà cờ `refund_status` không đồng bộ thời gian thực. | Không | Không |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | Không | **Đúng (cấp kinh doanh):** gộp cả 12 đơn `HCM-B2B` + hoàn trùng + email dài làm tổng tiết kiệm ròng rơi xuống `-60.486đ/ngày` (`ROI = -0,33`), đắt hơn làm tay. | Có thể góp phần gây đội chi phí & chạm trần ngân sách LLM. |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Chị Oanh (`NV-OANH`) và CFO phát hiện một đơn hàng bị chi tiền hoàn 2–3 lần trên sổ cái, gây thất thoát tiền thật và sai công nợ hãng | CFO thấy kho `HCM-B2B` vừa mất tiền chạy AI (`382đ–1.326đ`) vừa vẫn phải trả `10.000đ` công người duyệt (`review_rate = 100%`) → lỗ so với làm tay | CFO và Ops thấy chi phí LLM một ticket lên tới `2.412đ`, phá vỡ cam kết trần `1.500đ/ticket` đã thống nhất |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Khác (cổng đối chiếu sổ cái): `write_gate` cộng tổng tiền đã hoàn trong `ledger_rows(order_id=...)` để trừ vào quyền lợi còn lại, chặn ghi đúp | Khác (cổng phạm vi kinh doanh): loại kho `HCM-B2B` khỏi `business.pilot_scope`, trả thẳng đơn sỉ về quy trình tay (`10.000đ/ticket`) | Trao quyền kiểm soát cho người: đặt `business.cost_budget_per_ticket_vnd = 1100` để ticket quá dài chuyển thẳng sang người trước khi gọi LLM |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Ticket gửi lặp (`S5-02`, `S5-20`) bị cổng chặn ở `issue_refund` → trả lời khách "đã hoàn trước đó"; ca hoàn thiếu (`S5-21`) được sửa đúng số tiền còn lại `12.000đ` | Đơn kho `HCM-B2B` nằm ngoài `pilot_scope` → đi thẳng quy trình CSKH thủ công (`10.000đ`), không tốn `1đ` tiền LLM nào | Ticket có nội dung quá dài (sắp vượt `1.100đ` khi đọc) → `business_gate` chặn ngay trước khi đọc LLM, đẩy về hàng chờ `NV-HANH` xử lý tay |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | Sự kiện `refund_blocked_no_entitlement` và `refund_capped_to_entitlement` trong trace | Chỉ số kinh doanh mới `max_warehouse_cost_per_ticket_vnd` (và `escalated_after_llm_rate`) trong `monitors.py` | Sự kiện `business_gate` (`cost_budget_per_ticket_vnd`) và phân bố `cost_vnd` trong `monitors.py` |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| `orders.refund_status` và `ledger_seed` | Bản sao cập nhật theo batch đêm (`O-1017`), chủ yếu nghĩ tới khách gửi trùng ticket với AI | Trong thực tế còn có các giao dịch **CSKH hoàn tay trong ngày** (`T-CSKH-2520`, `T-CSKH-2521`, `basis = "manual"`) đã ghi vào `ledger` nhưng cờ `refund_status` vẫn `"NONE"`, kể cả trường hợp hoàn **một phần** (`O-2521` đã hoàn `10.000đ / 22.000đ`) | Nếu không tra `ledger_rows(order_id=...)` và trừ đi số tiền đã hoàn (`remaining = ent - already`), trợ lý hoàn đúp `20.000đ` (`O-2520`), hoàn thừa `10.000đ` (`O-2521`) và ghi thêm lỗi oan cho hãng |
| `orders.warehouse_id = "HCM-B2B"` và `goods_value_vnd` | Vòng 1 mới chỉ nhìn `goods_value_vnd` để tính thưởng trễ hạn, chưa hỏi mối liên hệ với `warehouse_id` và `auto_limit_vnd` | Kho sỉ `HCM-B2B` toàn đơn từ `2,2–3,4 triệu` (`O-2550..O-2561`), khi trễ `>= 7 ngày` mức bồi thường đều là `230.000đ > auto_limit_vnd (200.000đ)` nên **100% bị đẩy sang người duyệt** | Trợ lý không tự quyết được bất kỳ ca nào ở `HCM-B2B`: luôn tốn thêm tiền LLM (`382đ–1.326đ`) cộng `10.000đ` công người → mỗi ticket ở kho này luôn đắt hơn làm tay |
| `ticket.text` (kênh `email` kèm bảng kê) | Coi là chuỗi văn bản ngắn cần đọc để trích xuất ý định | Khách kho sỉ và một số khách lẻ dán nguyên bảng kê 55–75 dòng hàng (`SP-1000..`) vào email làm độ dài lên tới `> 7.000` ký tự (`read_cost` cộng `1đ / 4 ký tự`) | Đẩy tiền LLM lên tới `2.412đ/ticket` (> trần `1.500đ`); nếu `cost_budget_per_ticket_vnd` đặt sát `1.500đ` thì vẫn có thể bị cộng thêm `300đ` ở các bước LLM sau |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `issue_refund` (và luồng đọc đầu vào `llm.extract` / `pilot_scope`)

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `orders.refund_status` đi vào điều kiện kiểm tra đã hoàn | `WRONG` | Ticket `S5-20@11` (`O-2520`) và `S5-21@11` (`O-2521`): `refund_status` là `"NONE"` dù `ledger_seed` đã có dòng CSKH hoàn tay (`T-CSKH-2520`: `20.000đ`, `T-CSKH-2521`: `10.000đ`) | Hoàn trùng toàn bộ (`20.000đ`) hoặc hoàn lố (`22.000đ` thay vì `12.000đ`) → LogiX mất tiền ngân sách, chị Oanh lệch sổ đối soát; hãng `VNX`, `MKD` chịu lỗi phạt lặp | Mốc `base` chỉ kiểm cờ `refund_status`; cổng vòng 1 đã kiểm `ledger_rows(order_id=...)` | Cổng `write_gate` khi `tool == "issue_refund"` lấy `remaining = ent - sum(ledger_rows)` để chặn (`deny`) hoặc giảm đúng phần còn thiếu (`modify`) (**tầng chặn**). |
| `ticket.text` đi vào `llm.extract` (`read_cost`) | `PERTURBED` | Email `S5-54@11` (`O-2554`), `S5-50@11` (`O-2550`), `S5-70@11` (`O-2570`) dán kèm bảng kê 55–75 dòng mã hàng `SP-xxxx` khiến `cost_vnd` vọt lên `2.412đ` / `1.856đ` / `2.018đ` | Phá trần chi phí LLM `1.500đ/ticket` của Ops và làm đội chi phí dự án | `cost_budget_per_ticket_vnd = 1500` ở vòng 1 đã chặn các ticket rất dài nhưng còn lỏng nếu ticket ~1.250đ đọc xong bị cộng thêm `300đ` ở `policy_check + confirm` | Hạ `business.cost_budget_per_ticket_vnd = 1100` trong `config/operating_gates.json` (tính sẵn biên `300đ` cho các bước sau) (**tầng giới hạn thiệt hại / chặn đầu vào**). |
| `warehouse_id = "HCM-B2B"` đi vào `pilot_scope` | `INVALID` | 12 đơn kho sỉ `O-2550..O-2561` (`S5-50..S5-61`): giá trị `2,2–3,4 triệu`, mức bồi thường `230.000đ > auto_limit_vnd (200.000đ)` nên 100% `escalated` sau khi LLM đã đọc | Lãng phí tiền LLM + `10.000đ` công người cho toàn bộ 12 ticket/ngày (`10.382đ > 10.000đ` làm tay ở mốc `prepared`) | Chưa có gì ngăn ở vòng 1 vì `pilot_scope.mode = "all"` | Đặt `business.pilot_scope = {"mode": "warehouse", "warehouses": ["HN", "HCM", "DN", "CT"]}` loại kho `HCM-B2B` sang làm tay (**tầng vận hành / kinh doanh**). |
| Hàng chờ người duyệt khi giảm người trực (nhánh **chưa thấy trên trace hiện tại**) | `INCAPABLE` | Nếu giảm `reviewers_on_shift` xuống `1` (`6 ca/giờ`) mà đột ngột nhiều khách kho lẻ (`HN`, `HCM`, `DN`, `CT`) cùng gửi email dài `> 1.100đ` hoặc hàng giá trị cao `> 1,8 triệu` trong 1 giờ cao điểm | Hàng chờ ùn quá `30–60 phút` (`queue_stuck > 0`), phá vỡ lại SLA | Chưa có cảnh báo tự động theo kho và ngưỡng gọi thêm người khi giảm xuống 1 người | Chỉ số `monitors.py` (`max_warehouse_cost_per_ticket_vnd`) + Runbook giờ cao điểm gọi lại người thứ 2 khi chờ `>= 4 ca` hoặc `> 15 phút` (**tầng phát hiện & vận hành**). |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: (1) Tổng số tiền đã hoàn trên cùng `order_id` (gồm cả `ledger_seed` và các lệnh trong ngày) cộng với khoản hoàn mới không bao giờ được vượt quá `entitlement_vnd` tính từ tracking DB (`wrongful_refund_vnd == 0`); (2) Trong phạm vi pilot, không một kho/phân khúc nào có chi phí trung bình mỗi ticket vượt chi phí làm tay (`segments_worse_than_manual == 0`, tức `cost_per_ticket_vnd <= 10.000đ` ở mọi kho) và `llm_cost_max_per_ticket_vnd <= 1.500đ`.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): Hàm `write_gate` nhánh `issue_refund` trong `lab10/guards.py` (`remaining = ent - already`); các dòng `segments_worse_than_manual`, `cost.llm_cost_max_per_ticket_vnd` và `violations` trong báo cáo `lab10.eval` / `lab10.grade`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): Người thiết kế ngầm giả định rằng khách hàng viết ticket ngắn gọn như mẫu chat thường và CSKH không tự hoàn tiền thủ công trên cùng đơn hàng trong lúc chờ batch đối soát `refund_status` chạy vào ban đêm.

Vì sao có thể sai: Ngoài thực tế, khách hàng khiếu nại qua email (đặc biệt là khách cửa hàng/bán sỉ hoặc đơn nhiều mặt hàng) thường sao chép và dán nguyên bảng kê chi tiết hàng chục dòng mã hàng vào nội dung email làm tăng vọt chi phí đọc LLM; đồng thời khách hay nhắn đa kênh (gọi tổng đài CSKH rồi nhắn thêm app/Zalo) nên nhân viên CSKH có thể đã hoàn tay ngay trong ngày trước khi batch đêm đồng bộ cờ `refund_status`.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `<mã R-S5-before / R-S5-prepared>`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: Hệ thống trợ lý gây lỗ ròng và đắt hơn làm tay ở kho HCM-B2B (cho ai: LogiX-VN / CFO / chị Oanh, đo bằng: ROI = -0,33 ở base; kho HCM-B2B 11.326đ base / 10.382đ prepared > 10.000đ làm tay; hoàn sai 890.000đ ở base; LLM max 2.412đ)
 └─ HOẶC
 ├─ [1] Hoàn tiền trùng hoặc hoàn lố các đơn đã hoàn đa kênh / CSKH hoàn tay trong ngày — tầng: data / hành động
 │ └─ vì: agent chỉ đọc cờ `refund_status` cập nhật batch đêm thay vì kiểm tra `ledger_rows` thời gian thực trước khi ghi — bằng chứng: ticket `S5-02@11`, `S5-20@11`, `S5-21@11`, `ledger_seed` (`T-CSKH-2520`, `T-CSKH-2521`)
 ├─ [2] Kho sỉ `HCM-B2B` tốn cả tiền LLM lẫn 10.000đ công duyệt người (`100%` chuyển người) — tầng: kinh doanh (phạm vi pilot) / quyền hạn
 │ └─ vì: mọi đơn sỉ từ 2,2 triệu có mức bồi thường `230.000đ > auto_limit_vnd 200.000đ`, nhưng vẫn đưa toàn bộ vào `pilot_scope` (`all`) — bằng chứng: ticket `S5-51@11`, `O-2550..O-2561`, report prepared `kho HCM-B2B: 10.382đ > làm tay 10.000đ`
 └─ [3] Chi phí LLM mỗi ticket vượt trần `1.500đ` và định biên người trực chưa tối ưu — tầng: đầu vào / vận hành
 └─ vì: khách dán bảng kê 55–75 dòng hàng vào email (`read_cost` theo độ dài), cộng với bố trí 2 người trực (`60.000đ/ca` phí giữ chỗ) khi thực tế sau cắt kho sỉ chỉ còn 3 ca duyệt/ngày — bằng chứng: ticket `S5-54@11` (`2.412đ`), `S5-70@11` (`2.018đ`), report prepared `standby_cost_per_day_vnd = 60.000đ`
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Tổng tiền đã hoàn cho một đơn hàng trên `ledger` cộng khoản hoàn mới phải `<= entitlement_vnd` (`wrongful_refund_vnd == 0`) | Giả định mọi khoản hoàn trước đó đã kịp phản ánh vào cờ `orders.refund_status` (chỉ chạy batch đêm) và khách chỉ gửi 1 ticket cho 1 đơn |
| [2] | Chỉ đưa vào phạm vi tự động hoá những phân khúc/kho có khả năng tự động xử lý và chi phí `<= 10.000đ/ticket` (`segments_worse_than_manual == 0`) | Giả định mọi kho hàng đều có phân bố giá trị đơn tương tự đơn lẻ để phần lớn ticket nằm dưới hạn mức tự động `200.000đ` |
| [3] | Chi phí LLM mọi ticket phải `<= 1.500đ` và tổng chi phí giữ chỗ người trực không được vượt nhu cầu duyệt thực tế | Giả định khách hàng viết email khiếu nại ngắn gọn vài câu, không dán kèm toàn bộ bảng kê hàng chục dòng từ ERP/kho |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Hoàn trùng / hoàn lố đơn đã ghi trong `ledger_seed` hoặc gửi lặp đa kênh (`S5-02`, `S5-20`, `S5-21`) | `lab10/guards.py` → `write_gate` nhánh `tool == "issue_refund"`: cộng `already = sum(ledger_rows(order_id=...))`, tính `remaining = ent - already`, trả `deny` nếu `<= 0` hoặc `modify` về `remaining` (đã có từ vòng 1 và giữ nguyên ở vòng 2) | Chặn | **NGĂN hẳn** (với mọi giao dịch ghi chung trong `ledger`): lệnh ghi không thể hoàn quá `entitlement_vnd` tính từ DB; vẫn còn hở nếu CSKH hoàn tiền trên hệ thống ngoài không đồng bộ vào `ledger` | `<mã R-S5-after-...>` |
| [2] | Kho sỉ `HCM-B2B` đơn giá trị cao luôn vượt `auto_limit_vnd`, tốn cả LLM lẫn công người (`10.382đ > 10.000đ`) | `config/operating_gates.json` → `business.pilot_scope`: đổi từ `"all"` sang `{"mode": "warehouse", "warehouses": ["HN", "HCM", "DN", "CT"], "percent": 100}` (cắt kho `HCM-B2B` về làm tay `10.000đ/ticket`) | Vận hành & Kinh doanh | **NGĂN hẳn** lỗ tự động hoá cho kho sỉ `HCM-B2B` (độ phủ còn `0,6` = 18/30 ticket/ngày của 4 kho lẻ, `HCM-B2B` không tốn `1đ` tiền LLM nào) | `<mã R-S5-after-...>` |
| [3] | Email dán bảng kê dài vượt trần LLM `1.500đ` + dư phí giữ chỗ `2` người trực (`60.000đ/ngày`) | `config/operating_gates.json` → hạ `business.cost_budget_per_ticket_vnd` từ `1500` xuống `1100` (chừa biên `300đ` cho `policy_check + confirm`) và chỉnh `operations.reviewers_on_shift` từ `2` xuống `1` (`review_capacity_per_hour = 6`); thêm `max_warehouse_cost_per_ticket_vnd` trong `lab10/monitors.py` | Giới hạn thiệt hại, Vận hành & Phát hiện | **NGĂN hẳn** chi phí LLM vượt `1.500đ/ticket` (`llm_cost_max = 665đ`) nhờ cổng ngân sách trước `llm.extract`; chỉ **GIẢM** rủi ro chi phí người trực (xuống `3.897đ/ticket`, `ROI = 1,57`, `wait_max = 0 phút`) vì nếu lưu lượng kho lẻ tăng đột biến giờ cao điểm vẫn cần gọi thêm người thứ 2 | `<mã R-S5-after-...>` |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `max_warehouse_cost_per_ticket_vnd` (chỉ số kinh doanh theo kho cho thẻ S5) |
| **Bước / hành vi được đo** | Tổng chi phí vận hành thực tế (tiền máy LLM + công người duyệt/kiểm lại) trên **từng kho hàng** nằm trong phạm vi pilot |
| **Thước đo** (một câu, có đơn vị) | Chi phí trung bình mỗi ticket của **kho hàng tốn kém nhất** trong phạm vi pilot (đơn vị: đồng/ticket), tách riêng 2 dòng cấu phần tiền máy (`cost_vnd`) và công người (`review_cost`) trên từng kho |
| **Dữ liệu** (trường nào của trial, không có nhãn) | Các trường không nhãn của mỗi `trial` trong `trials`: `warehouse`, `cost_vnd` (tiền máy + nền tảng), `status`, `review_kind` ("escalated" hoặc "recheck"), `amount_vnd` (để theo dõi tổng tiền hoàn). Không dùng nhãn đúng/sai |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Nhóm toàn bộ `trials` theo `wh = t["warehouse"] or "?"`. Với mỗi kho `wh`: `tiền_máy_tb = sum(t["cost_vnd"]) / len(sub)`; `công_người_tb = sum(10000 nếu t["status"] == "escalated" else (4000 nếu t["review_kind"] == "recheck" có note else 0)) / len(sub)`. Chi phí kho = `tiền_máy_tb + công_người_tb`. Chỉ số trả về `max` trên các kho có `len(sub) > 0`; nếu `trials` rỗng trả về `0` |
| **Khung thời gian / ngưỡng báo động** | Tính theo **từng ca 480 phút (hàng ngày)**: **Ngưỡng VÀNG**: `> 8.000đ/ticket` (tiệm cận mức tiết kiệm tối thiểu 20%); **Ngưỡng ĐỎ**: `> 10.000đ/ticket` (kho đó đã đắt hơn làm tay — loại ngay kho khỏi `business.pilot_scope`) |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không thấy tiền mất do hoàn sai (`wrongful_refund_vnd`, vì không có nhãn trong production) và không tính được phần chi phí cố định giữ chỗ người trực (`30.000đ/người/ca`) phân bổ riêng vào từng kho |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | Trước khi sửa (base): bộ nền `10.359đ` (kho `"?"`, còn `DN = 4.586đ`) · thẻ S5 `11.326đ` (kho `HCM-B2B`). Sau khi sửa (after): bộ nền `10.359đ` (`"?"`) · thẻ S5 `4.214đ` (kho `HN`, không còn kho nào `> 10.000đ`) — hai giá trị khác biệt rõ rệt, monitor sáng đèn đúng chuẩn |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `<mã R-S5-after / R-S5-grade-...>`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Hệ thống trợ lý gây lỗ ròng hoặc chi phí kho vượt làm tay (> 10.000đ) hoặc vượt trần LLM 1.500đ
 └─ HOẶC
 ├─ [1] Hoàn trùng/lố đơn đã hoàn trong ngày VÀ [cổng `write_gate` (`issue_refund` kiểm `ledger_rows`) hỏng HOẶC CSKH hoàn ở sổ ngoài]
 ├─ [2] Kho sỉ `HCM-B2B` tốn cả LLM lẫn công người VÀ [cổng `business.pilot_scope` loại `HCM-B2B` bị tắt/đổi lại `all`]
 └─ [3] Email dài vượt trần `1.500đ` hoặc dư người trực đội chi phí VÀ [cổng `cost_budget_per_ticket_vnd = 1100` & `reviewers_on_shift = 1` + monitor `max_warehouse_cost_per_ticket_vnd` cùng hỏng] (còn hở khi lưu lượng giờ cao điểm dồn gấp 3)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `lab10/guards.py` → `write_gate` (`issue_refund` kiểm `ledger_rows` và `remaining`) | Chặn | **Ngăn hẳn** trong phạm vi sổ cái chung (`wrongful_refund_vnd = 0đ`) | Nếu nhân viên CSKH hoàn tiền qua kênh/tool khác chưa đồng bộ ngay vào bảng `ledger` thì cổng chưa thấy |
| [2] | `config/operating_gates.json` → `business.pilot_scope` (`mode = "warehouse"`, chỉ giữ `["HN", "HCM", "DN", "CT"]`) | Vận hành & Kinh doanh | **Ngăn hẳn** lỗ ở kho `HCM-B2B` (0 ticket kho sỉ đi qua LLM; `segments_worse_than_manual = 0`) | Nếu một kho lẻ (như `HN`) phát sinh nhiều đơn giá trị cao `> 1,8 triệu` trễ `>= 7 ngày` thì tỉ lệ chuyển người ở kho đó tăng mạnh |
| [3] | `business.cost_budget_per_ticket_vnd = 1100`, `operations.reviewers_on_shift = 1`, `lab10/monitors.py` → `max_warehouse_cost_per_ticket_vnd` | Giới hạn thiệt hại, Vận hành & Phát hiện | **Ngăn hẳn** vượt trần LLM `1.500đ` (`llm_cost_max = 665đ`); **Giảm** chi phí/ticket còn `3.897đ` (`ROI = 1,57`) | Với `1` người trực (`6 ca/giờ`), nếu nhiều email dài cùng chuyển sang hàng chờ trong giờ cao điểm thì phải gọi thêm người theo Runbook |
| [1] | | | | |
| [2] | | | | |
| [3] | | | | |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Một kho lẻ trong 4 kho pilot có chi phí mỗi ticket vượt `10.000đ` (do tăng số email dài bị chuyển người từ ngưỡng `1.100đ` hoặc đơn giá trị cao khi `REFUND-v4` hạ hạn mức tự động còn `100.000đ` từ `2026-12-01`) | Trung bình | Cao (làm kho đó đắt hơn làm tay và kéo `ROI` giảm) | `Phạm Quỳnh Anh` | `max_warehouse_cost_per_ticket_vnd` (`monitors.py`) `> 8.000đ` (Vàng) hoặc `> 10.000đ` (Đỏ); `ops.cost.roi < 0.25` | Tắt trợ lý tại kho vượt ngưỡng bằng cách bỏ tên kho đó khỏi `business.pilot_scope.warehouses` và cập nhật ngày xem lại tiêu chí | Quyết định **Thu hẹp** thêm phạm vi kho trước Gate 2 nếu xảy ra | `MANAGE` |
| Giảm xuống `1` người trực (`6 ca/giờ`) gây ùn hàng chờ khi giờ cao điểm hoặc khi nhiều ca `> 1.100đ` bị đẩy sang người cùng lúc | Trung bình | Trung bình–Cao (phá SLA `30–60 phút` hoặc tăng phí giữ chỗ khi gọi thêm người) | `Lê Xuân Phúc` | `ops.queue.wait_max_min > 20 phút` (Vàng) / `> 30 phút` (Đỏ); `ops.queue.stuck >= 1`; `escalation_rate > 0.35` | Kích hoạt quy trình Runbook giờ cao điểm: `NV-HANH` gọi thêm người trực thứ 2 (biết trước phí tăng `30.000đ/ca`), nếu vẫn ùn thì chuyển sang Thu hẹp tỷ lệ `%` | Buộc giữ phạm vi `Thu hẹp` chứ không mở rộng `all` ở Gate 2 | `MEASURE` / `MANAGE` |
| Công cụ hoàn tay của CSKH ghi chậm hoặc nằm ngoài bảng `ledger` khiến `write_gate` không phát hiện được khoản hoàn trùng trong ngày | Thấp–Trung bình | Cao (phát sinh `wrongful_refund_vnd > 0đ`, kích hoạt `stop_condition`) | `Lê Xuân Phúc` | `wrongful_refund_vnd > 0đ` khi chị Oanh (`NV-OANH`) đối soát cuối ngày | `NV-TUNG` tắt ngay `"issue_refund": "off"` trong `config/switches.json` tới khi đồng bộ realtime bảng `ledger` với tool nội bộ CSKH | Chuyển quyết định sang **Dừng** hoặc **Cải tiến thêm** nếu tái diễn | `GOVERN` |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 2 (Dữ liệu) | Xong | Đã mở lại bản đồ dữ liệu ở mục C3.5 cho `ledger_seed`, kho `HCM-B2B` và độ dài `email` | `Lê Xuân Phúc` |
| 5 (Hiệu năng, hạ tầng) | Xong | Đặt `cost_budget_per_ticket_vnd = 1100` (`llm_cost_max = 665đ <= 1.500đ`), `1` người trực (`6 ca/giờ`), `wait_max = 0,0 phút`, `0 ca ùn` trên cả `S5` và `base` | `Phạm Quỳnh Anh` |
| 6 (Chi phí) | Xong | Sau khi loại `HCM-B2B`: chi phí toàn hệ thống trên `S5` còn `3.897đ/ticket` (rẻ hơn `10.000đ` làm tay), `ROI = 1,57`, tiết kiệm `109.857đ/ngày`, `segments_worse_than_manual = 0` | `Phạm Quỳnh Anh` |
| 7 (Vận hành) | Xong | Đã thêm chỉ số `max_warehouse_cost_per_ticket_vnd` trong `lab10/monitors.py` (sáng đèn: `base` `10.359đ` vs `S5` `4.214đ`), cập nhật Runbook 4–5 (mục C11) | `Lê Xuân Phúc` |
| 9 (Quyết định) | Xong | Chốt quyết định v2 (**Thu hẹp** kho `HCM-B2B`) ở mục C12 khớp hoàn toàn bằng chứng 3 mốc và tiêu chí đã ký | `Vũ Đức Minh` |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Tín hiệu **Chi phí mỗi ticket so với làm tay** ở Runbook 2 lẽ ra phải báo trước, nhưng vòng 1 mới nhìn trung bình chung (`5.565đ`) và kho `"?"`, **chưa có chỉ số tách riêng chi phí theo từng kho** (`HCM-B2B`) và chưa tách **tỉ lệ chuyển người sau khi đã đọc LLM**; vòng 2 đã bổ sung `max_warehouse_cost_per_ticket_vnd` vào `lab10/monitors.py`. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | (1) Hạ `business.cost_budget_per_ticket_vnd` từ `1.500đ` xuống `1.100đ` (chừa biên `300đ` cho các bước LLM sau); (2) Bổ sung ngưỡng báo động ĐỎ cho `max_warehouse_cost_per_ticket_vnd`: `> 10.000đ/ticket` thì loại kho khỏi pilot; (3) Thêm điều kiện dừng theo kho vào `operations.stop_conditions`. |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Sau khi loại `HCM-B2B` (giảm từ `15` xuống chỉ còn `3` ca duyệt/ngày), giảm `operations.reviewers_on_shift` từ `2` xuống `1` người trực (`6 ca/giờ`, tiết kiệm `30.000đ/ca` phí giữ chỗ); giữ nguyên `NV-TUNG` làm PIC, `NV-HANH` đứng tên duyệt/gọi người dự phòng, `NV-OANH` đối soát. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Đổi `business.pilot_scope` từ `"all"` sang `"warehouse"` chỉ chạy 4 kho lẻ `["HN", "HCM", "DN", "CT"]` (độ phủ `0,6`), trả toàn bộ `12 ticket/ngày` của kho sỉ `HCM-B2B` về làm tay từ đầu để không mất tiền LLM vô ích; giữ `decision_note = false`, `review_sampling_pct = 0` vì chưa có sự cố mất lòng tin của CSKH. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | Không lộ PII hay trừ tiền shop; các hãng (`GHSH`, `VNX`, `MKD`) bị phạt lặp ở mốc `base` đã được chặn từ cổng `write_gate`. Chị `Phạm Kiều Oanh (NV-OANH)` đối soát bảng công nợ sạch với các hãng trước `17h00` cùng ngày; `Vũ Đức Minh` cùng `Lê Thanh Tùng (NV-TUNG)` gửi bảng chi phí mới (`ROI = 1,57`, loại `HCM-B2B`) báo cáo CFO trước `17h00`. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | `pii_leaks = 0` ở cả `base`, `prepared`, `after` (cổng `notify_carrier` và `legal.pii_fields_blocked_to_third_party` đã lọc sạch `recipient_contact` và `customer_note`); không có dữ liệu cá nhân nào rời hệ thống. |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Lộ qua **phản hồi của người** (email CFO gửi lúc `09:30` kèm bảng chi phí 2 tuần và phản ánh của chị Oanh về đơn hoàn 2–3 lần), đối chiếu lại mới thấy số trên từng kho. Nguồn bàn chưa có ở vòng 1 là **công cụ báo cáo chi phí tự động hàng ngày theo từng kho và trạng thái đồng bộ trực tiếp giữa tool hoàn tay của CSKH với sổ cái `ledger`**. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp `3` lần trong một giờ (lên `~9–12 ticket/giờ`, hàng chờ chạm `>= 4 ca` hoặc thời gian chờ `> 20 phút`) thì: `NV-HANH` gọi ngay `1` người trực dự phòng vào ca (tăng `reviewers_on_shift` từ `1` lên `2`, công suất `12 ca/giờ`); nếu sau khi thêm người vẫn có ca chờ vượt `30 phút` hoặc `queue_stuck >= 1` thì `NV-TUNG` thu hẹp `business.pilot_scope` sang `mode = "percent", percent = 50` và đẩy phần dôi ra về làm tay.
2. Nếu nhà cung cấp LLM lỗi quá `10` phút (tỉ lệ `llm_error 429` vượt `10%` hoặc `confirm` retry liên tiếp) thì: kiểm tra ngay cổng `write_gate` giữ nguyên chống ghi đúp; `NV-TUNG` thông báo lên `Nhóm Zalo Trực Hoàn tiền` và tạm chuyển `"issue_refund": "off"` trong `config/switches.json` để toàn bộ ca hoàn chuyển về hàng chờ thủ công của `NV-HANH` tới khi API ổn định trở lại.
3. Nếu người duyệt báo không tin một quyết định của trợ lý (nghi ngờ dùng sai phê duyệt hoặc phải kiểm lại thủ công) thì: `NV-TUNG` khoá tạm tự động hoá đối với các khoản có dấu hiệu lệch sổ, bật ngay `"decision_note": true` và `"review_sampling_pct": 10` trong `config/operating_gates.json` với người đứng tên là `NV-HANH` (khớp `staff_behavior.trust_conditions`), đồng thời chị `NV-OANH` đối chiếu lại toàn bộ `ledger` trong ngày trước khi chạy tiếp.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `531f9c0` (giống v1; ký đầu `26d92b3`) |
| Hash chốt cổng vòng 1 | `1b8aeb58` (giống v1) |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: `<R-S5-before-...>` · prepared: `<R-S5-prepared-...>` · after: `<R-S5-after-...>` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | **Không** (`violations: []` trên cả `S5` và `base`: chờ tối đa `0,0 phút`, `0 ca ùn`, chi phí `3.897đ/ticket`, `ROI = 1,57`, `llm_cost_max = 665đ <= 1.500đ`, hoàn tự động `98.000đ <= 1.500.000đ`, `0` lỗi oan, `0` lộ PII) |
| Kho hoặc hãng có số xấu nhất: kho `HN` (`4.214đ/ticket`, `review_rate = 0,375`). Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Không đổi: dù kho `HN` có chi phí cao nhất trong 4 kho lẻ (`4.214đ/ticket` vì chứa các email dài như `S5-70`, `S5-73` bị chuyển người bởi ngưỡng `1.100đ`), mức này vẫn rẻ hơn rất nhiều so với làm tay `10.000đ/ticket` (`worse_than_manual = false`). Trước khi sửa, kho xấu nhất là `HCM-B2B` (`10.382đ > 10.000đ`) và đã được cắt bỏ. |
| Quyết định (khoanh một) | **Thu hẹp** |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `<R-S5-after-...>` (`S5 · after`): cả 5 chỉ số bắt buộc và 3 chỉ số `business_ops` đều đạt (`pass_rate = 1,0`, `pass_k = 1,0`, `wrongful_refund_vnd = 0đ`, `wrongful_carrier_faults = 0`, `pii_leaks = 0`, `escalation_rate = 0,1667 <= 0,35`, `cost = 3.897đ <= 10.000đ`, `ROI = 1,57 >= 0,2`, `queue_stuck = 0`) |
| Bằng chứng 2 | So sánh 3 mốc trên `S5`: từ `base` (`pass_rate = 0,8333`, hoàn sai `890.000đ`, `ROI = -0,33`, `HCM-B2B = 11.326đ`) → `prepared` (`pass_rate = 1,0`, hoàn sai `0đ`, `ROI = 0,33`, nhưng `HCM-B2B = 10.382đ` vẫn vượt làm tay) → `after` (`cost = 3.897đ`, `ROI = 1,57`, tiết kiệm `109.857đ/ngày`, `0` vượt trần) |
| Bằng chứng 3 | Bộ nền `<R-base-after-...>`: `pass_rate = 1,0`, `pass_k = 1,0`, `0` ca mới hỏng (`regression ok`), chi phí `4.202đ/ticket`, `ROI = 1,38`, `coverage = 1,0`; chỉ số `max_warehouse_cost_per_ticket_vnd` sáng đèn (`base` `10.359đ` vs `S5` `4.214đ`) |
| Khớp dòng nào trong `decision_rule` đã ký? | Khớp điều kiện **"Thu hẹp"** (và bảo vệ phần đang lỗ vốn): chỉ tiếp tục chạy thử có kiểm soát trên **4 kho lẻ (`HN, HCM, DN, CT`)** đạt toàn bộ ngưỡng an toàn và kinh doanh, **cắt bỏ hoàn toàn kho sỉ `HCM-B2B`** vì tự động hoá ở kho này về mặt cấu trúc không thể có lời (`10.382đ > 10.000đ` làm tay). |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | Cắt toàn bộ kho sỉ **`HCM-B2B`** (`12 ticket/ngày`, chiếm `40%` tổng lượng ticket của gói `S5`); giữ lại **`60%` (`coverage = 0,6` = `18 ticket/ngày`)** ở 4 kho lẻ `["HN", "HCM", "DN", "CT"]`; bố trí **`1` người trực/ca** (`6 ca/giờ`); toàn bộ ticket kho `HCM-B2B` (và đơn kho lẻ dài vượt `1.100đ`) chuyển thẳng sang quy trình CSKH thủ công (`10.000đ/ticket`) do chị Trần Thị Hạnh (`NV-HANH`) điều phối. |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | Không áp dụng |
| Nếu Dừng: bài học ghi lại | Không áp dụng |
| Ngày quyết định lại (trừ khi Dừng) | `2026-11-30` (ngay trước khi `REFUND-v4` có hiệu lực `2026-12-01`) |
| PIC ký | `NV-TUNG` (Lê Thanh Tùng) |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: **Giữ hướng `Thu hẹp`** nhưng **đổi cụ thể đối tượng bị cắt**: v1 mới dự kiến cắt các đơn không tra được (`kho "?"` tốn `10.359đ`), sang v2 xác định và cắt dứt điểm **kho sỉ `HCM-B2B`** (`12 ticket/ngày` tốn `10.382đ > 10.000đ` làm tay ở mốc `prepared`), đồng thời hạ trần đọc LLM xuống `1.100đ` và giảm người trực về `1`, giúp chi phí giảm từ `7.491đ` xuống `3.897đ/ticket` và `ROI` tăng từ `0,33` lên `1,57`.
- Report tự kiểm tra: mã lần chạy `<R-S5-grade-...>` · ô nào còn đỏ (nguyên nhân × tầng): sau khi Kỹ sư cổng thêm `max_warehouse_cost_per_ticket_vnd` vào `lab10/monitors.py` và chạy lại `grade`, các mục `visible`, `regression`, `monitor` đều xanh (`—` ở `hidden` do chỉ team chấm có test ẩn; lưu ý mục `criteria` còn cần Coach xác nhận về lịch sử commit `531f9c0`).
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: Đỡ được hoàn toàn **`890.000đ` hoàn trùng/lố** từ `ledger_seed` và tin nhắn lặp đa kênh, giảm `20` lỗi hãng oan về `0`, chặn email dài `2.412đ` xuống `665đ` (`pass_rate` tăng từ `0,8333` lên `1,0`, `ROI` từ `-0,33` lên `+0,33`). Bỏ sót việc đưa kho sỉ `HCM-B2B` (luôn vượt `auto_limit_vnd 200.000đ`) vào tự động gây lỗ ở kho này (`10.382đ/ticket`) và đặt dư `2` người trực.
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: Report mốc `after` ghi `được phép cân nhắc "Tiếp tục"` (do `violations: []` và `signed_criteria_not_met: []`), nhưng bàn chủ động chọn **`Thu hẹp`** (cắt kho sỉ `HCM-B2B`, giữ 4 kho lẻ độ phủ `0,6`) — hoàn toàn hợp lệ và khớp chặt với bằng chứng từ CFO vì chính cấu hình `Thu hẹp` này mới tạo ra bảng số sạch `ROI = 1,57` ở mốc `after`.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: Bộ thử hiện tại chưa có gói chuyển sang **`REFUND-v4` từ `2026-12-01`** (giảm `auto_limit_vnd` từ `200.000đ` xuống `100.000đ`), điều này có thể làm nhiều đơn ở 4 kho lẻ trước đây tự động được nay phải chuyển sang người duyệt — do đó bắt buộc giữ quyết định **Thu hẹp** có kiểm soát và hẹn xem lại vào `2026-11-30`.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Thiết kế hiện tại giả định các yêu cầu hoàn tiền của khách sỉ và khách lẻ được gửi ngắn gọn đúng trọng tâm và mọi khoản hoàn tiền của CSKH đều được ghi nhận đầy đủ vào cùng sổ cái trước khi trợ lý xử lý; ngoài thực tế khách sỉ kho HCM-B2B thường dán bảng kê 50–75 dòng hàng hoá đẩy chi phí LLM lên 2.412đ/ticket (> trần 1.500đ) và CSKH có thể hoàn tay trong ngày trước khi cờ refund_status kịp cập nhật lúc nửa đêm.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Hệ thống cổng kết hợp code và config NGĂN hẳn được hoàn trùng/hoàn lố từ sổ cái (guards.py chặn theo ledger_rows), NGĂN hẳn lỗ tự động hoá ở kho sỉ HCM-B2B (business.pilot_scope cắt kho sỉ, giữ 4 kho lẻ độ phủ 0,6), và NGĂN hẳn chi phí LLM vượt trần 1.500đ (business.cost_budget_per_ticket_vnd = 1.100đ); tuy nhiên cổng chỉ GIẢM khả năng ngập hàng chờ với 1 người trực vì nếu lưu lượng tăng gấp ba ngoài dự kiến hoặc CSKH hoàn tay ở công cụ ngoài không ghi chung vào ledger thì vẫn cần bổ sung người trực hoặc tắt bớt công tắc.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Vì data hiện tại là mock, trong pilot thật tại 4 kho lẻ (HN, HCM, DN, CT) trước Gate 2 cần đo lại: (1) giá trị đơn hàng, độ dài email thực tế và tỉ lệ đơn kho lẻ vượt hạn mức 100.000đ khi chuyển sang chính sách REFUND-v4 từ 2026-12-01; (2) độ trễ cập nhật giữa sổ hoàn tay của CSKH với hệ thống trợ lý; (3) thời gian duyệt ca thực tế của người trực (có giữ được <= 10 phút/ca ở giờ cao điểm với 1 người trực hay không) và chi phí token LLM thực tế theo từng kho.
