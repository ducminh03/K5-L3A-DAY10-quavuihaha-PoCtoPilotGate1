# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): quavuihaha
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-quavuihaha-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S5

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên       | MSSV        | Vai                    | Trưởng nhóm |
| --: | --------------- | ----------- | ---------------------- | :---------: |
|   1 | Vũ Đức Minh     | 2A202603673 | Sản phẩm và kinh doanh |      x      |
|   2 | Lê Xuân Phúc    | 2A202603655 | Vận hành và pháp lý    |             |
|   3 | Phạm Quỳnh Anh  |             | Sản phẩm và kinh doanh |             |
|   4 | Mai Đăng Khương |             | Kỹ sư cổng             |             |
|   5 |                 |             |                        |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

# <<<<<<< Updated upstream

## LeXuanPhuc-2A202603655

### Phần việc phụ trách

- Vai trong bàn: **Vận hành và pháp lý**.
- Phụ trách file: `config/operating_gates.json` (phần `operations`, `legal` và phối hợp chỉnh Vòng 2 theo thẻ `S5`), `submission/submission.json` (`team`, `members`, `decision_v1`, `decision_v2`, `three_lines`).
- Phụ trách phiếu:
  - `templates/form-a-criteria.md`: hoàn thiện tiêu chí A1–A5 (cùng trưởng nhóm).
  - `templates/form-b-evaluation-gates.md`: mục B3 (bản đồ dữ liệu & ví dụ drift), B4 (HAZOP mở rộng ngoài kỹ thuật: Người duyệt, Dữ liệu bên thứ ba, Ngân sách, CSKH kiểm lại), B5 (Checklist nhóm 2, 7, 8), B7.5–B7.6 (Runbook phần 1–3 và Giờ cao điểm).
  - `templates/form-c-incident.md` (thẻ `S5`): C0–C2, C3.5 (mở lại bản đồ dữ liệu cho `ledger_seed`, kho `HCM-B2B`, độ dài email), C4–C11 (HAZOP `S5`, đặc tả chỉ số `max_warehouse_cost_per_ticket_vnd`, Risk register, cập nhật Checklist & Runbook phần 4–5), C12 (quyết định v2 và 3 dòng bắt buộc).

### Đóng góp cụ thể

- Thiết lập đầy đủ các cổng vận hành và pháp lý vòng 1 (`NV-TUNG`, `NV-HANH`, `NV-OANH`, kênh báo tin Zalo, 5 điều kiện dừng, chặn trường PII `recipient_contact` & `customer_note`, bắt buộc có nguyên nhân trễ mới ghi lỗi hãng) và viết Runbook 1–3 + kịch bản giờ cao điểm khớp thông số vòng 1.
- Rà soát xung đột merge ở vòng 2 cho `templates/form-b-evaluation-gates.md` (giữ đúng thông số vòng 1 đã chốt ở `config/operating_gates.round1.json`) và `config/operating_gates.json` (giữ cấu hình vòng 2 cho `S5`).
- Phân tích nguyên nhân chi phí ở thẻ `S5`: loại kho sỉ `HCM-B2B` (luôn vượt `auto_limit_vnd 200.000đ` nên 100% chuyển người duyệt, tốn `10.382đ/ticket > 10.000đ` làm tay) khỏi `business.pilot_scope`, hạ `business.cost_budget_per_ticket_vnd` từ `1500` xuống `1100` (chừa biên `300đ` cho `policy_check + confirm`), và tối ưu `operations.reviewers_on_shift` từ `2` xuống `1` (`6 ca/giờ`). Kết quả đánh giá `S5` mốc `after` giảm chi phí từ `7.491đ` (`prepared`) xuống `3.897đ/ticket`, `ROI = 1,57`, `0` ca ùn, `0` vượt trần; bộ `base` giữ `100%` pass (`4.202đ/ticket`, `ROI = 1,38`).
- Xây dựng Risk register (mục C10), cập nhật Checklist go-live và Runbook 4–5 (mục C11) cho tuần chạy thử thật, và hoàn thiện phần tổng hợp `submission/submission.json`.

### Bằng chứng

- Commit: `441cce7`, `a302474` (xử lý conflict và cập nhật phiếu/cấu hình Vòng 2); chạy kiểm tra `python3 -m unittest discover -s tests` (13/13 OK) và `lab10.eval.evaluate` cho `S5` & `base` mốc `after` (sẽ bổ sung mã `runs/R-S5-grade-...` sau khi Kỹ sư cổng hoàn tất `lab10/monitors.py` và chạy `lab10.grade`).
- Dòng trong phiếu: `templates/form-a-criteria.md` (`A1`–`A5`), `templates/form-b-evaluation-gates.md` (`B3`, `B4`, `B5`, `B7.5`–`B7.6`), `templates/form-c-incident.md` (`C1`, `C3.5`, `C8`, `C10`, `C11`, `C12`).
- Cấu hình & bài nộp: `config/operating_gates.json`, `submission/submission.json`.

### Exit ticket

- **Một điều học được:** Cổng kiểm soát và phân tích rủi ro không chỉ chặn lỗi kỹ thuật trên từng dòng code mà phải kiểm chéo ở cấp **đơn vị kinh tế theo phân khúc** và **trình tự chi phí thực tế** (loại kho `HCM-B2B` vì luôn đẩy sang người sau khi tốn tiền LLM, và đặt ngân sách đọc email `1.100đ` có biên an toàn cho các bước gọi sau).
- **Một điều còn chưa chắc:** Khi chính sách `REFUND-v4` có hiệu lực ngày `2026-12-01` (hạ `auto_limit_vnd` từ `200.000đ` xuống `100.000đ`), tỉ lệ ca vượt hạn mức tự động ở 4 kho lẻ sẽ tăng tới đâu và `1` người trực (`6 ca/giờ`) có giữ được hàng chờ dưới `30 phút` trong giờ cao điểm thật hay không (đã đưa vào mục cần đo lại trước Gate 2).

> > > > > > > Stashed changes

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
