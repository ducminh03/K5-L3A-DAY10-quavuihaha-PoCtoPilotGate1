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
|   3 | Phạm Quỳnh Anh  | 2A202603671 | Sản phẩm và kinh doanh |             |
|   4 | Mai Đăng Khương | 2A202603627 | Kỹ sư cổng             |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## LeXuanPhuc-2A202603655

### Phần việc phụ trách

- Vai trong bàn: **Vận hành và pháp lý**.
- Phụ trách file: `config/operating_gates.json` (mục `operations`, `legal`, phối hợp phạm vi `pilot_scope` ở Vòng 2), `submission/submission.json` (`team`, `members`, `incident`, `decision_v1`, `decision_v2`, `three_lines`).
- Phụ trách phiếu:
  - `templates/form-a-criteria.md`: mục A1.2 (góc nhìn chị Oanh, chị Hạnh) và A2 câu 1.4 (telemetry production).
  - `templates/form-b-evaluation-gates.md`: mục B3 (bản đồ dữ liệu & ví dụ drift), B4 (HAZOP mở rộng ngoài kỹ thuật), B5 (Checklist nhóm 2, 8), B7.5–B7.6 (Runbook phần 1–3 và Giờ cao điểm).
  - `templates/form-c-incident.md` (thẻ `S5`): mục C3.5 (mở lại bản đồ dữ liệu cho `ledger_seed` và kho `HCM-B2B`), C4, C11 (Runbook phần 4–5 cho tuần đầu chạy thử thật).

### Đóng góp cụ thể

- Thiết lập đầy đủ cổng vận hành và pháp lý vòng 1 trong `config/operating_gates.json` (`NV-TUNG` giữ công tắc, `NV-HANH` đứng tên duyệt, `2` người trực/`12` ca/giờ, `max_queue_wait_minutes = 30`, kênh báo tin Zalo, điều kiện dừng, chặn PII `recipient_contact` & `customer_note`, bắt buộc nguyên nhân trễ trong tracking khi ghi lỗi hãng) khớp với Runbook 1–3 và kịch bản giờ cao điểm.
- Phối hợp rà soát bài nộp Vòng 2 (thẻ `S5`): giữ `2` người trực (`12` ca/giờ) và trần `cost_budget_per_ticket_vnd = 1500` cùng `pre_guard` cắt text dài; cắt kho sỉ `HCM-B2B` khỏi `business.pilot_scope` (giữ 4 kho lẻ `HN, HCM, DN, CT`, độ phủ `0,6`) → chi phí giảm từ `7.491đ` (`prepared`) xuống `3.989đ/ticket`, `ROI = 1,51`, `0` ca ùn, `0` vượt trần; bộ `base` giữ `100%` pass (`5.565đ/ticket`, `ROI = 0,8`).
- Viết Runbook 4–5 ứng phó tuần đầu chạy thử thật (tách tín hiệu theo kho/chỉ số `escalated_llm_cost_avg_vnd` & `warehouse_escalation_rate_max`, đối soát hoàn tay CSKH trước khi trả lời khách, xử lý giờ cao điểm ×3, LLM lỗi quá 15 phút, và bật kiểm mẫu khi mất lòng tin).
- Hoàn thiện danh sách thành viên khớp `TEAM.md` và `three_lines` trong `submission/submission.json`.

### Bằng chứng

- Commit: `f570223` (và tham gia xử lý Vòng 2 cùng nhóm qua nhánh/tài khoản repo bàn `441cce7`, `385e852`).
- Mã lần chạy đối chiếu: `R-base-prepared-20261118-160601-f29414`, `R-S5-after-20261118-172409-208603`, `R-S5-grade-20261118-173609-c671aa` (`PASS-VISIBLE`: `1 integrity ✅`, `2 criteria ✅`, `3 visible ✅`, `5 regression ✅`, `6 monitor ✅`).
- Dòng trong phiếu: `templates/form-a-criteria.md` (`A1.2`, `A2`), `templates/form-b-evaluation-gates.md` (`B3`, `B4`, `B5`, `B7.5`–`B7.6`), `templates/form-c-incident.md` (`C3.5`, `C4`, `C11`).
- Cấu hình & bài nộp: `config/operating_gates.json`, `submission/submission.json`.

### Exit ticket

- **Một điều học được:** Không thể chỉ kiểm tra an toàn kỹ thuật hoặc chi phí trung bình toàn hệ thống; phải bóc tách cả cấu trúc vận hành theo từng kho (kho sỉ `HCM-B2B` tốn `10.382đ/ticket` dù `pass_rate = 1,0`) và giữ đồng bộ chặt giữa quy trình hoàn tay của CSKH với sổ cái `ledger`.
- **Một điều còn chưa chắc:** Ngoài thực tế chi phí làm tay đối với đơn sỉ kho `HCM-B2B` có đúng `10.000đ` như mock hay cao hơn, và tốc độ đồng bộ giữa công cụ hoàn tay của CSKH với `ledger` có gây độ trễ trong ca hay không (đã đưa vào mục cần đo lại ở Runbook 4 và `three_lines.measure_in_pilot`).

## PhamQuynhAnh-2A202603671

### Phần việc phụ trách

- Vai: **Sản phẩm và kinh doanh**.
- File: `config/acceptance_criteria.json` (nhóm `business_ops`), `config/operating_gates.json` (mục `business`).
- Phiếu: A (A1, A4), B (B3, B5 nhóm 5–6, B6, B7.4, B8), C thẻ `S5` (C1, C2, C5, C7–C8, C11 nhóm 6, C12).

### Đóng góp cụ thể

- **Vòng 1:** Đặt ngưỡng `business_ops` (`cost_per_ticket_vnd_max = 10000`, `roi_min = 0.2`, `queue_stuck_max = 0`) và cổng `business` (`daily_refund_cap_vnd = 1.500.000` = 75% ngân sách Finance, `cost_budget_per_ticket_vnd = 1500`, `roi_min = 0.25`); đề xuất quyết định v1 **Thu hẹp**.
- **Vòng 2 (S5):** Phân tích chi phí theo kho, chỉ ra kho sỉ `HCM-B2B` luôn vượt `auto_limit 200.000đ` nên 100% chuyển người (`10.382đ/ticket` > `10.000đ` làm tay). Đề xuất `pilot_scope` chỉ giữ 4 kho lẻ → chi phí `7.491đ` → `3.989đ/ticket`, ROI `0,33` → `1,51`, bộ `base` không suy giảm.
- Kiểm chứng 2 chỉ số theo dõi kinh doanh (`escalated_llm_cost_avg_vnd`, `warehouse_escalation_rate_max`) và cập nhật Checklist nhóm 6 (Chi phí).

### Bằng chứng

- Commit (đẩy chung qua tài khoản git nhóm `2A202603673`): `26d92b3` (ký tiêu chí), `531f9c0` (chỉnh ngưỡng), `f7e1f56` (cổng `business` + phiếu B).
- Lần chạy: `R-base-prepared-20261118-160601-f29414`, `R-S5-after-20261118-172409-208603`, `R-S5-grade-20261118-173609-c671aa` (`PASS-VISIBLE`).

### Exit ticket

- **Học được:** Phải bóc chi phí theo từng phân khúc/kho, không nhìn trung bình toàn hệ thống — có nhóm AI chỉ làm đội thêm tiền.
- **Chưa chắc:** Chi phí làm tay mock cố định `10.000đ` cho cả đơn sỉ; và tỉ lệ chuyển người ở 4 kho lẻ khi `REFUND-v4` hạ hạn mức xuống `100.000đ` (từ `2026-12-01`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
