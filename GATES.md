# GATES — Bậc năng lực L0–L7 và cách đo

**Luật chung**
- Chỉ lên bậc khi PASS gate. Gate làm vào Chủ nhật (`GATE <LANG> L#`), ~10' mỗi ngôn ngữ.
- FAIL → agent chẩn đoán loại lỗi → 2–3 ngày luyện trúng lỗi → retest bằng đề MỚI tương đương.
- PASS → ghi vào `tracker/skills.md`, đặt lịch ôn sau 1 / 3 / 7 / 14 ngày. Lần ôn nào dưới ngưỡng → **REVIEW**.
- Mỗi kỹ năng đi qua 4 trạng thái: **K** biết → **R** nhận ra khi nghe → **U** dùng được khi có gợi ý → **A** tự động (≤3s, trong hội thoại). Gate yêu cầu ít nhất **U**. L3 trở lên yêu cầu **A**.
- Đo phản xạ: dùng voice mode; tôi đếm "1-2-3" trong đầu hoặc bấm giờ điện thoại. Không có voice → tự khai báo trung thực.

## Ngưỡng
| Loại | EN (ngưỡng gốc) | ZH/KO/JA (beginner) | Lý do chỉnh |
|---|---|---|---|
| Kiến thức (biết nghĩa) | ≥90% | ≥90% | — |
| Nhận ra khi nghe | ≥85% | ≥85% | — |
| Nghe hiểu | ≥80% | ≥80% (L0–L4) · ≥70% (L5) | Nghe tự nhiên sau 10 tuần là quá sức với beginner nếu giữ 80% |
| Nói đúng | ≥80% | ≥80% | — |
| Nói trôi | ≥75% | ≥70% | Beginner cần thời gian xử lý |
| Phản xạ pattern quen | ≤3s | ≤3s (L2+), ≤5s (L0–L1) | Mới làm quen hệ âm |
| Test đời thực | ≥80% | ≥75% | Trần thực tế sau 12 tuần |

## Các bậc

### L0 — ÂM (ZH/KO/JA: W1–2 · EN: W1–3, xem `en/sounds.md`)
| Test | Số câu | Ngưỡng |
|---|---|---|
| Phân biệt cặp âm/thanh (agent đọc 1 trong 2, tôi chọn) | 20 | ≥85% |
| Nhận âm: nghe từ → ghi phiên âm/thanh số | 10 | ≥85% |
| Đọc to 10 chunk, agent chấm phát âm | 10 | ≥80% |
| (EN) Nhận connected speech: nghe câu nhanh → viết đầy đủ | 10 | ≥85% |

### L1 — TỪ LÕI + REPAIR (W3–4)
| Test | Số câu | Ngưỡng |
|---|---|---|
| Nghe chunk → nói nghĩa | 20 (lấy ngẫu nhiên từ 50) | ≥90% |
| Nghĩa tiếng Việt → nói chunk | 15 | ≥80%, ≤5s |
| 5 repair phrase trong tình huống bất ngờ | 5 | 100% |

### L2 — KHUNG CÂU (W5–6)
| Test | Số câu | Ngưỡng |
|---|---|---|
| Drill 8 bước trên 10 pattern ngẫu nhiên | 10 pattern × 3 bước | ≥80% đúng, ≤3s |
| Nghe câu mới (từ cũ, ghép kiểu mới) → hiểu | 10 | ≥85% |

### L3 — HỘI THOẠI NGẮN (W7)
| Test | Ngưỡng |
|---|---|
| 3 đoạn hỏi–đáp 4–6 lượt, không xem bài, chủ đề lõi | ≥80% lượt đáp đúng ý, ≤3s |
| Ít nhất 1 lần tự hỏi ngược lại + 1 lần dùng repair | Có / không |

### L4 — TÌNH HUỐNG HẰNG NGÀY (W8–9)
| Test | Ngưỡng |
|---|---|
| Role-play 4 tình huống ngẫu nhiên (ăn uống, mua sắm, đường đi, hẹn), agent cài 1 từ lạ mỗi tình huống | ≥80% hoàn thành nhiệm vụ; xử lý được từ lạ bằng repair |

### L5 — NGHE TỰ NHIÊN (W10–11)
| Test | Ngưỡng |
|---|---|
| 3 audio chưa nghe bao giờ, 2 giọng khác nhau, tốc độ chậm–vừa (EN: tốc độ thật) | Hiểu ý chính EN ≥80% / beginner ≥70% |
| Chép chính tả 3 câu | ≥75% từ đúng |
| Chẩn đoán: % lỗi theo loại (ÂM/WEAK/NỐI/RÚT/TÁCH/TỪ/ĐOÁN/TRUY/TỐC) | Ghi vào dashboard |

### L6 — NÓI LIÊN TỤC (W10–11)
| Test | Ngưỡng |
|---|---|
| Kể chuyện/giải thích (EN 3', beginner 2') | Fluency ≥75% / ≥70%; không im lặng quá 5s |
| Giải thích 3 thứ không biết tên bằng từ đơn giản | 3/3 người nghe đoán đúng |

### L7 — HỘI THOẠI THẬT (W12, có thử trước ở W4/W6/W8/W10)
Lệnh `REAL <LANG>`. Agent không báo trước tình huống (vd gặp đồng nghiệp lần đầu).
| Tiêu chí (mỗi mục 0–2 điểm) |
|---|
| Giới thiệu bản thân · Trả lời tự nhiên · Hỏi ngược lại · Phản ứng (thật à, hay quá…) · Hỏi thêm chi tiết · Xin nhắc lại/làm rõ · Xử lý từ không biết · Giữ hội thoại đủ giờ (EN 10' / beginner 5') |
Điểm = tổng / 16. PASS EN ≥80%, beginner ≥75%.

## % lộ trình
`% = (số gate PASS + 0.5 × gate đang luyện) / 8 × 100`. Gate bị REVIEW tính 0.5 đến khi PASS lại.
