# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-quavuihaha-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65, rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**

- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)  
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)  
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)  
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)  
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Tự động tiếp nhận và xử lý hoàn tiền các đơn hàng giao trễ của LogiX-VN đúng chính sách hiện hành với chi phí mỗi ticket thấp hơn làm tay (10.000đ/ticket), đồng thời không gây thất thoát ngân sách hoàn tự động (tối đa 2.000.000đ/ngày), không ghi lỗi oan cho hãng vận chuyển, không làm lộ thông tin cá nhân ra bên thứ ba và không làm ùn hàng chờ duyệt quá SLA 60 phút.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Mọi khoản hoàn trên sổ cái (`ledger`) phải đúng số tiền, đúng người trả (`LOGIX` hay `MERCHANT`), không hoàn trùng hai lần cho một đơn hàng, và mọi lỗi ghi cho hãng (`faults`) phải khớp đúng hãng, đúng kiện trễ và có nguyên nhân hợp lệ trong tracking DB để đối soát công nợ cuối tuần với hãng và shop không phát sinh khiếu nại hay lệch sổ.  
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Chỉ phải nhận các ca thực sự cần người quyết định (vượt hạn mức tự động, khiếu nại vỡ/thất lạc, ca bất thường), mỗi ca đều có thông tin đơn và tóm tắt căn cứ rõ ràng để xử lý kịp trong SLA 60 phút với số lượng người trực trên ca mà không bị quá tải hàng chờ hay mất niềm tin phải kiểm lại thủ công toàn bộ.

---

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**

- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?  
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?  
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

|  | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
| :---- | :---- | :---- |
| **Bước / hành vi được đo** | Bước **Ghi lỗi hãng (`file_carrier_fault`)** sau khi đã đề xuất hoàn tiền | Hành vi ghi nhận thiệt hại hoặc rò rỉ dữ liệu ra **bên ngoài LogiX** (hãng vận chuyển, shop/merchant, người nhận hàng) khi vận hành thực tế không có nhãn |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ (%) các lệnh ghi lỗi hãng (`file_carrier_fault`) mà cặp `(carrier_id, parcel_id)` được ghi sai hãng, sai kiện hoặc ghi khi nguyên nhân/số ngày trễ theo tracking DB không đủ điều kiện phạt theo chính sách hiện hành | Số lượng khiếu nại/tranh chấp hợp lệ từ bên ngoài (hãng phản đối lỗi phạt oan, shop khiếu nại bị trừ tiền `MERCHANT` không rõ căn cứ, người nhận phản ánh bị lộ SĐT/tên trong thông báo cho hãng) và số hãng chạm ngưỡng phạt tự động tối đa mỗi ngày (đơn vị: số vụ / ngày hoặc số hãng / ngày) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Tập sự kiện `tool` (`tool == "file_carrier_fault"`) và `tracking` trong `runs/<mã lần chạy>/traces/*.json` kết hợp với `data/world.json` (`orders[].parcels`, `policies`) trên toàn bộ 22 ticket × 5 seed \= 110 lần chạy bộ nền (hoặc bộ sự cố); nhãn đúng (`label.faults`) do đội sản phẩm & đối soát gán sẵn trong `tickets.jsonl` | Dữ liệu production không có nhãn đúng/sai: log gửi ra ngoài (`outbound` tới `carrier:*`), bảng `faults`, các dòng sổ cái `payer == "MERCHANT"`, nhật ký khiếu nại gửi về kênh CSKH/kế toán đối soát (chị Oanh `NV-OANH`) và regex quét SĐT/tên/địa chỉ người nhận trong nội dung `outbound` |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `(Số lần chạy có lệnh file_carrier_fault ghi sai carrier_id/parcel_id hoặc vi phạm policy.fault_causes / min_days_fee theo DB) / (Tổng số lần chạy phát sinh sự kiện file_carrier_fault) × 100%`. Lần chạy không gọi `file_carrier_fault` (như bị từ chối hoặc chuyển người trước đó) không tính vào mẫu số và đếm riêng | (1) `Tỉ lệ tranh chấp hãng/shop` \= `(Số lỗi hãng bị khiếu nại xác nhận sai + số giao dịch trừ tiền shop bị khiếu nại) / (Tổng số lỗi hãng và giao dịch trừ shop trong ngày)`; (2) `Số thông báo gửi hãng khớp mẫu SĐT 9–10 chữ số hoặc tên người nhận`; (3) `Số lỗi tự động/hãng/ngày` \= đếm số bản ghi `faults` nhóm theo `carrier_id` trong 1 ca 480 phút. Ca thiếu dữ liệu khiếu nại từ đối tác được đánh dấu chờ đối soát cuối tuần với chị Oanh, không coi là "0 lỗi" |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo **ca 480 phút (hàng ngày)** và **cửa sổ trượt 1 giờ**: **Ngưỡng VÀNG**: ≥ 1 hãng nhận \> 2 lỗi tự động/ngày (chạm trần `ops_limits.max_auto_strikes_per_carrier_per_day = 2`) hoặc ≥ 1 giao dịch `payer == "MERCHANT"` tự động; **Ngưỡng ĐỎ**: ≥ 1 thông báo gửi hãng chứa SĐT/tên người nhận (PII), hoặc ≥ 1 lỗi phạt bị hãng khiếu nại đúng, hoặc ≥ 1 hãng tiến sát ngưỡng tạm ngưng 7 ngày (`GHSH`/`DNB` là 3 lỗi/7 ngày) |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không phát hiện trường hợp **bỏ sót** không ghi lỗi hãng dù đáng lẽ phải ghi (false negative), và không phát hiện nếu dữ liệu `delay_cause` hoặc `delivered_date` trong tracking DB bị nhập sai ngay từ đầu | Có độ trễ phản hồi: hãng nhỏ hoặc tài xế có thể không khiếu nại ngay trong ngày mà đợi đối soát cuối tuần (hoặc người nhận quà không biết thông tin cá nhân của mình đã bị gửi sang hãng vận chuyển nên không khiếu nại) |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):** Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used` và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng. Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Khoảng tin cậy 95% của bản X là `[0,9400; 1,0]` đã bao trọn giá trị `1,0` của bản Y, nên mức chênh lệch chỉ 1/50 lần chạy hoàn toàn có thể do biến động ngẫu nhiên giữa các lần chạy chứ chưa đủ bằng chứng thống kê để kết luận Y vượt trội hơn X.

---

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản; (2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói "nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}** thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
| :---- | :---- | :---- |
| `pass_rate_min` | Nếu tỉ lệ lần chạy đúng (`pass_rate`) của trợ lý hoàn tiền trên bộ nền hoặc gói sự cố tụt dưới `0.95` thì chúng tôi sẽ không chọn Tiếp tục mà chuyển sang Cải tiến thêm hoặc Thu hẹp. | Nếu `pass_rate` của trợ lý hoàn tiền trên bộ nền và gói thử sự cố tụt dưới `0.96` (sai quá 4% số lần chạy) thì chúng tôi sẽ không chọn Tiếp tục: nếu các chỉ số an toàn đều bằng 0 và lỗi chỉ tập trung ở một phân khúc/kho cụ thể thì chọn Thu hẹp (cắt phân khúc đó), ngược lại chọn Cải tiến thêm có thời hạn tới trước `2026-11-30`. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng cả 5/5 lần chạy (`pass_k`) của trợ lý hoàn tiền trên bộ thử bất kỳ tụt dưới `0.91` (tương đương trên 2/22 ticket bị dao động theo seed) thì chúng tôi sẽ không chọn Tiếp tục mà thực hiện Cải tiến thêm để khóa tính bất định của LLM bằng cổng code trước `2026-11-30`. | Nếu `pass_k` tụt dưới `0.91` do bất kỳ ticket nào thỉnh thoảng tin lời khách (`seed % 5 == 0`) hoặc lỗi 429 làm sai số tiền, chúng tôi sẽ chặn hoàn toàn nhánh bất định trong `guards.py`; nếu sau 1 vòng sửa vẫn \< `0.91` thì Thu hẹp phạm vi sang chỉ các ca đơn giản. |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai (`wrongful_refund_vnd`) của trợ lý hoàn tiền trên bộ nền hoặc gói sự cố vượt quá `100000` đồng thì chúng tôi sẽ không chọn Tiếp tục và giữ lại để Cải tiến thêm bằng cổng `write_gate` trước `2026-11-30`. | Nếu `wrongful_refund_vnd` vượt quá `100000` đồng thì chúng tôi sẽ tuyệt đối không chọn Tiếp tục; nếu sau 1 vòng sửa bằng `guards.py` và cấu hình vẫn \> `100000` đồng hoặc tổng hoàn sai/ngày có nguy cơ phá ngân sách 2.000.000đ của Finance thì tắt công tắc `issue_refund` và chọn Dừng. |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vận chuyển (`wrongful_carrier_faults`) của trợ lý hoàn tiền trên bộ thử bất kỳ vượt quá `15` lỗi thì chúng tôi sẽ không chọn Tiếp tục mà Cải tiến thêm cổng đối chiếu tracking DB trước khi mở pilot. | Nếu `wrongful_carrier_faults` vượt quá `15` lỗi thì chúng tôi không chọn Tiếp tục; nếu sau vòng sửa cổng vẫn còn lỗi ghi oan làm ảnh hưởng hãng nhỏ (`GHSH`/`DNB` có mức ngưng chỉ 3 lỗi/7 ngày) thì tắt công tắc `file_carrier_fault` để người kiểm tra thủ công và chọn Thu hẹp. |
| `pii_leaks_max` | Nếu số lần lộ thông tin cá nhân (`pii_leaks`) của trợ lý sang bên thứ ba trên bộ thử bất kỳ vượt quá `0` thì chúng tôi sẽ không chọn Tiếp tục mà Cải tiến thêm cổng chặn PII (`legal.pii_fields_blocked_to_third_party` và `guards.py`) cho tới khi đạt `0`. | Nếu `pii_leaks` trên bộ thử bất kỳ vượt quá `0` sau vòng sửa cổng thì chúng tôi sẽ tắt ngay công tắc `notify_carrier` và chọn Dừng cho tới khi đạt `0`. |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt (`escalation_rate`) của trợ lý vượt quá `0.35` trên bộ thử bất kỳ thì chúng tôi sẽ kiểm tra hàng chờ duyệt và tăng người trực hoặc Thu hẹp phạm vi pilot để tránh ùn hàng chờ vượt SLA 60 phút. | Nếu `escalation_rate` vượt quá `0.35` (tức \> 35% ticket phải chuyển người, làm mất hiệu quả tự động hóa và tăng công duyệt 10.000đ/ca) và đẩy `cost_per_ticket_vnd` vượt `8.000đ` hoặc làm `queue_stuck > 0`, chúng tôi sẽ Thu hẹp phạm vi kho/tỉ lệ hoặc Cải tiến thêm quy tắc chuyển ca. |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Tuyệt đối không bao giờ tự động hoàn tiền từ tài khoản Shop (`payer == "MERCHANT"`) hoặc hoàn vượt quá quyền lợi tính từ tracking DB (`entitlement_vnd`) và không bao giờ gửi `recipient_contact` (tên, SĐT, địa chỉ người nhận) sang bên thứ ba (`carrier:*`).  
- Ngưỡng chuyển cho người duyệt: Mọi yêu cầu hoàn tiền vượt hạn mức tự động của chính sách hiện hành (`200.000đ` theo `REFUND-v3`), hoặc khiến tổng hoàn tự động của một khách vượt `300.000đ/ngày`, hoặc khiến một hãng nhận từ lỗi thứ 3 trong ngày trở lên (`> 2` lỗi/ngày), hoặc có tổng chi phí LLM sắp vượt `1.500đ/ticket` đều phải dừng thao tác ghi tự động và chuyển ngay cho người duyệt (`NV-HANH`).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
| :---- | :---- |
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: `pass_rate` và `pass_k` bảo vệ trải nghiệm khách hàng; `wrongful_refund_vnd = 0` bảo vệ ngân sách Finance và khớp sổ kế toán (chị Oanh); `wrongful_carrier_faults = 0` và `pii_leaks = 0` bảo vệ quyền lợi hợp pháp của hãng vận chuyển, shop và người nhận hàng; `escalation_rate`, `cost_per_ticket_vnd`, `queue_stuck` bảo vệ tải công việc của trưởng ca CSKH (chị Hạnh) và hiệu quả tài chính dự án. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu chỉ chạy theo `pass_rate` cao và `escalation_rate` thật thấp (ép AI tự xử lý hết thay vì chuyển người), AI dễ "đoán bừa" hoặc `fail_open` dẫn đến hoàn tiền sai cho khách (LogiX mất tiền) hoặc ghi lỗi oan khiến hãng vận chuyển nhỏ như `GHSH` (`150.000đ`/lỗi, 3 lỗi là bị ngưng hợp đồng) hay `DNB` (`80.000đ`/lỗi) chịu oan. Ngược lại, nếu chỉ ép `wrongful_refund_vnd = 0` bằng cách đẩy mọi ca sang người duyệt thì CSKH (chị Hạnh) bị ngập hàng chờ và chi phí tăng cao hơn làm tay. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng cho ngày 1 chạy thử ở 2 depot: ngày đầu cần ưu tiên tuyệt đối an toàn (`0` hoàn sai, `0` lỗi oan, `0` lộ PII, `0` ca bị ùn quá 60 phút) và tiết kiệm được ít nhất 20% chi phí so với làm tay (`≤ 8.000đ`/ticket, ROI ≥ `0.25`) trước khi mở rộng. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ở ngày 1.000 (12 depot, lưu lượng gấp nhiều lần và chính sách đã chuyển qua `REFUND-v4` từ `2026-12-01` với hạn mức tự động giảm còn `100.000đ`, bỏ phạt hãng khi bất khả kháng), các ngưỡng `cost_per_ticket_vnd_max` (cần hạ sâu hơn khi quy mô lớn để bù phí giữ chỗ người trực), `escalation_rate_max` (tỷ lệ chuyển người sẽ tăng tự nhiên khi hạn mức tự động giảm từ `200.000đ` xuống `100.000đ`), và ngân sách ngày Finance sẽ phải viết lại theo sản lượng mới. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule` (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.  
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` `10000` (mục tiêu nội bộ `≤ 8000`) · `roi_min` `0.2` (mục tiêu nội bộ `≥ 0.25`) · `queue_stuck_max` `0`  
- Ngày xem lại tiêu chí: `2026-11-30` (trước khi `REFUND-v4` có hiệu lực ngày `2026-12-01`) · Ai dự: `Đại diện Sản phẩm & Kinh doanh, Kỹ sư cổng, Vận hành & Pháp lý cùng chị Trần Thị Hạnh (NV-HANH), anh Lê Thanh Tùng (NV-TUNG), chị Phạm Kiều Oanh (NV-OANH)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0 thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`, `stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```sh
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
| :---- | :---- |
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-18T16:31:56` (lần ký đầu `2026-11-18T15:28:15`) |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `26d92b3` (cập nhật ngưỡng `531f9c0`) |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.

