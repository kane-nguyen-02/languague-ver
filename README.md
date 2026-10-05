# Nghe-nói 4 ngôn ngữ cùng AI agent (05/10 → 30/12/2026)

EN (intermediate) · ZH · KO · JA (beginner). 12 tuần, ~90'/ngày, 6 ngày/tuần + Chủ nhật test.

## Bắt đầu trong 2 phút
1. Mở AI agent (Claude, ChatGPT voice…). Dán khối trong [`AGENT_PROMPT.md`](AGENT_PROMPT.md).
   Nếu agent đọc được repo này (vd Claude Code), chỉ cần nói: "Đọc AGENT_PROMPT.md và bắt đầu".
2. Xem hôm nay là tuần nào ở [`ROADMAP.md`](ROADMAP.md).
3. Buổi đầu: `DIAG EN` (xếp bậc EN). Sau đó gõ lệnh, vd `ZH W1D1`, rồi `JA W1D1`, `KO W1D1`, `EN W1D1`. Danh sách lệnh: [`COMMANDS.md`](COMMANDS.md).
4. Cuối buổi: dán khối LOG vào `tracker/log.md`, cập nhật `tracker/skills.md` + `errors.md`. Chủ nhật: `ÔN HẠN` → `GATE` → `DASH`.

**Luật vàng:** chỉ lên bậc khi PASS gate. Học xong bài không có nghĩa là PASS.

## Nghe là phải NGHE
Đọc transcript không luyện được tai. Dùng voice mode / TTS của app AI cho mọi `NGHE` và `SHADOW`. Nói thành tiếng mọi câu, kể cả khi học một mình.

## Cấu trúc
| File | Dùng để |
|---|---|
| `AGENT_PROMPT.md` | Luật dạy + vòng đo–sửa–retest cho agent (v2) |
| `GATES.md` | Bậc L0–L7: test, ngưỡng PASS, cách chấm, % lộ trình |
| `ROADMAP.md` | Lịch 12 tuần, bậc ↔ tuần, phân bổ giờ, lịch gate |
| `COMMANDS.md` | Lệnh học + lệnh đo (DIAG/GATE/RETEST/ÔN HẠN/REAL/DASH) + bảng repair |
| `TOPICS.md` | 20 chủ đề (10 lõi cho ZH/KO/JA) + template |
| `<lang>/sounds.md` | Hệ âm gắn ưu tiên P0–P3 + Gate L0 (EN = sound map đầy đủ) |
| `<lang>/patterns.md` | 30 khung câu + 20 động từ cốt lõi |
| `<lang>/chunks.md` | Chunks theo chủ đề |
| `<lang>/weeks.md` | Bài từng ngày W1–W12 |
| `tracker/dashboard.md` | % lộ trình, 6 chỉ số, top 3 nút thắt |
| `tracker/skills.md` | Trạng thái K/R/U/A + lịch ôn 1/3/7/14 ngày |
| `tracker/errors.md`, `log.md` | Lỗi (có loại lỗi) + nhật ký buổi |

`<lang>` = `en`, `zh`, `ko`, `ja`.
