# Hướng Dẫn GSD (Get Shit Done)

**GSD** tạo kế hoạch dự án phân cấp, tối ưu cho phát triển solo với Claude Code.

---

## Bắt Đầu Nhanh

1. `/gsd-new-project` — Khởi tạo dự án (nghiên cứu, yêu cầu, lộ trình)
2. `/gsd-plan-phase 1` — Tạo kế hoạch chi tiết cho giai đoạn đầu
3. `/gsd-execute-phase 1` — Thực thi giai đoạn

**Vòng lặp cốt lõi:**
```
/gsd-new-project → /gsd-plan-phase → /gsd-execute-phase → lặp lại
```

---

## Khởi Tạo Dự Án

### `/gsd-new-project`
Khởi tạo dự án mới qua luồng hợp nhất.

- Hỏi sâu để hiểu bạn đang xây dựng gì
- Nghiên cứu domain tùy chọn (4 agent song song)
- Định nghĩa yêu cầu với phạm vi v1/v2/ngoài phạm vi
- Tạo lộ trình với phân chia giai đoạn và tiêu chí thành công

**Tạo các file `.planning/`:**
| File | Mô tả |
|------|-------|
| `PROJECT.md` | Tầm nhìn và yêu cầu |
| `config.json` | Chế độ workflow (interactive/yolo) |
| `REQUIREMENTS.md` | Yêu cầu có REQ-ID |
| `ROADMAP.md` | Các giai đoạn ánh xạ tới yêu cầu |
| `STATE.md` | Bộ nhớ dự án |

### `/gsd-map-codebase`
Lập bản đồ codebase hiện có (dự án brownfield).

- Phân tích codebase với các agent song song
- Tạo `.planning/codebase/` với 7 tài liệu
- Dùng **trước** `/gsd-new-project` khi có code sẵn

---

## Lập Kế Hoạch Giai Đoạn

### `/gsd-discuss-phase <số>`
Giúp diễn đạt tầm nhìn trước khi lập kế hoạch.

- Ghi lại cách bạn hình dung giai đoạn hoạt động
- Tạo `CONTEXT.md` với tầm nhìn, điều cần thiết, ranh giới
- Dùng khi bạn có ý tưởng về giao diện/cảm nhận

```
/gsd-discuss-phase 2
/gsd-discuss-phase 2 --batch
/gsd-discuss-phase 2 --batch=3
```

### `/gsd-research-phase <số>`
Nghiên cứu hệ sinh thái toàn diện cho domain phức tạp.

- Khám phá stack chuẩn, pattern kiến trúc, bẫy phổ biến
- Tạo `RESEARCH.md` với kiến thức "chuyên gia xây thế nào"
- Dùng cho: 3D, game, audio, shader, ML, và domain chuyên biệt

```
/gsd-research-phase 3
```

### `/gsd-list-phase-assumptions <số>`
Xem Claude định làm gì trước khi bắt đầu.

- Hiển thị cách tiếp cận dự định của Claude
- Cho phép chỉnh hướng nếu Claude hiểu nhầm
- Không tạo file — chỉ output hội thoại

```
/gsd-list-phase-assumptions 3
```

### `/gsd-plan-phase <số>`
Tạo kế hoạch thực thi chi tiết cho giai đoạn cụ thể.

- Tạo `.planning/phases/XX-tên/XX-YY-PLAN.md`
- Chia giai đoạn thành tasks cụ thể, có thể thực hiện
- Bao gồm tiêu chí xác minh và đo lường thành công

```
/gsd-plan-phase 1
→ Tạo: .planning/phases/01-foundation/01-01-PLAN.md
```

> **PRD Express:** Truyền `--prd path/to/requirements.md` để bỏ qua discuss-phase khi đã có tiêu chí chấp nhận rõ ràng.

---

## Thực Thi

### `/gsd-execute-phase <số>`
Thực thi tất cả kế hoạch trong giai đoạn.

- Nhóm kế hoạch theo wave, thực thi wave tuần tự
- Các kế hoạch trong cùng wave chạy **song song**
- Flag `--wave N` chỉ thực thi Wave N
- Xác minh mục tiêu giai đoạn sau khi hoàn thành
- Cập nhật `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`

```
/gsd-execute-phase 5
/gsd-execute-phase 5 --wave 2
```

---

## Bộ Định Tuyến Thông Minh

### `/gsd-do <mô tả>`
Tự động định tuyến văn bản tự do đến lệnh GSD phù hợp.

- Phân tích ngôn ngữ tự nhiên để tìm lệnh phù hợp nhất
- Hỏi khi không rõ ràng
- Dùng khi bạn biết muốn gì nhưng không biết lệnh nào

```
/gsd-do sửa nút đăng nhập
/gsd-do refactor hệ thống auth
/gsd-do tôi muốn bắt đầu milestone mới
```

---

## Chế Độ Nhanh

### `/gsd-quick [--full] [--validate] [--discuss] [--research]`
Thực thi task nhỏ với đảm bảo GSD, bỏ qua agent tùy chọn.

- Task nhanh lưu trong `.planning/quick/`
- Cập nhật `STATE.md` (không cập nhật `ROADMAP.md`)

| Flag | Ý nghĩa |
|------|---------|
| `--full` | Pipeline đầy đủ: discuss + research + kiểm tra + xác minh |
| `--validate` | Kiểm tra kế hoạch và xác minh sau thực thi |
| `--discuss` | Thảo luận nhẹ để phát hiện vùng xám |
| `--research` | Agent nghiên cứu cách tiếp cận trước khi lập kế hoạch |

```
/gsd-quick
/gsd-quick --full
/gsd-quick --research --validate
```

### `/gsd-fast "mô tả"`
Thực thi task nhỏ inline — không subagent, không file kế hoạch.

- Dùng cho: sửa typo, thay đổi config, thêm đơn giản
- Tối đa 3 file chỉnh sửa
- Commit nguyên tử với message chuẩn

```
/gsd-fast "sửa typo trong README"
/gsd-fast "thêm .env vào gitignore"
```

---

## Quản Lý Lộ Trình

### `/gsd-add-phase "mô tả"`
Thêm giai đoạn mới vào cuối milestone hiện tại.

### `/gsd-insert-phase <sau> "mô tả"`
Chèn giai đoạn khẩn cấp dưới dạng số thập phân.

```
/gsd-insert-phase 7 "Sửa lỗi auth nghiêm trọng"
→ Tạo: Giai đoạn 7.1
```

### `/gsd-remove-phase <số>`
Xóa giai đoạn tương lai và đánh số lại các giai đoạn sau.

```
/gsd-remove-phase 17
→ Giai đoạn 17 bị xóa, 18-20 trở thành 17-19
```

---

## Quản Lý Milestone

### `/gsd-new-milestone "tên"`
Bắt đầu milestone mới qua luồng hợp nhất.

```
/gsd-new-milestone "Tính năng v2.0"
/gsd-new-milestone --reset-phase-numbers "Tính năng v2.0"
```

### `/gsd-complete-milestone <phiên bản>`
Lưu trữ milestone đã hoàn thành, chuẩn bị cho phiên bản tiếp theo.

- Tạo entry `MILESTONES.md` với thống kê
- Lưu trữ chi tiết đầy đủ
- Tạo git tag cho bản phát hành

```
/gsd-complete-milestone 1.0.0
```

---

## Theo Dõi Tiến Độ

### `/gsd-progress`
Kiểm tra trạng thái dự án và định tuyến đến hành động tiếp theo.

- Hiển thị thanh tiến độ trực quan và % hoàn thành
- Tóm tắt công việc gần đây từ file SUMMARY
- Liệt kê quyết định chính và vấn đề mở

---

## Quản Lý Phiên

### `/gsd-resume-work`
Tiếp tục công việc từ phiên trước với khôi phục context đầy đủ.

### `/gsd-pause-work`
Tạo handoff context khi tạm dừng giữa chừng.

---

## Gỡ Lỗi

### `/gsd-debug "mô tả vấn đề"`
Gỡ lỗi có hệ thống với trạng thái bền vững qua nhiều phiên.

- Thu thập triệu chứng qua hỏi thích ứng
- Điều tra bằng phương pháp khoa học
- Tồn tại qua `/clear` — chạy `/gsd-debug` không có args để tiếp tục
- Lưu trữ vấn đề đã giải quyết

```
/gsd-debug "form submit lỗi im lặng"
/gsd-debug   ← tiếp tục phiên đang hoạt động
```

---

## Ghi Chú Nhanh

### `/gsd-note <văn bản>`
Ghi lại ý tưởng không ma sát — một lệnh, lưu ngay.

```
/gsd-note refactor hệ thống hook
/gsd-note list
/gsd-note promote 3
/gsd-note --global ý tưởng xuyên dự án
```

---

## Quản Lý Todo

### `/gsd-add-todo [mô tả]`
Ghi lại ý tưởng hoặc task từ hội thoại hiện tại.

```
/gsd-add-todo                         ← suy ra từ hội thoại
/gsd-add-todo Thêm refresh token auth
```

### `/gsd-check-todos [khu vực]`
Liệt kê todo đang chờ và chọn một để làm.

```
/gsd-check-todos
/gsd-check-todos api
```

---

## Kiểm Thử Chấp Nhận

### `/gsd-verify-work [giai đoạn]`
Xác nhận tính năng đã xây dựng qua UAT hội thoại.

- Trích xuất deliverable có thể kiểm thử từ SUMMARY.md
- Trình bày lần lượt từng bài test (trả lời có/không)
- Tự động chẩn đoán thất bại và tạo kế hoạch sửa

```
/gsd-verify-work 3
```

---

## Phát Hành

### `/gsd-ship [giai đoạn]`
Tạo PR từ công việc giai đoạn đã hoàn thành.

```
/gsd-ship 4
/gsd-ship 4 --draft
```

### `/gsd-review --phase N [--all]`
Đánh giá ngang hàng đa AI — gọi các CLI AI ngoài để review kế hoạch.

```
/gsd-review --phase 3 --all
```

### `/gsd-pr-branch [target]`
Tạo nhánh sạch cho PR bằng cách lọc các commit `.planning/`.

```
/gsd-pr-branch
/gsd-pr-branch main
```

---

## Kiểm Toán Milestone

### `/gsd-audit-milestone`
Kiểm toán hoàn thành milestone so với ý định ban đầu.

### `/gsd-audit-uat`
Kiểm toán xuyên giai đoạn tất cả mục UAT còn tồn đọng.

### `/gsd-plan-milestone-gaps`
Tạo giai đoạn để bù đắp khoảng trống được xác định qua kiểm toán.

---

## Cấu Hình

### `/gsd-settings`
Cấu hình toggle workflow và profile model tương tác.

### `/gsd-set-profile <profile>`
Chuyển nhanh profile model cho các agent GSD.

| Profile | Mô tả |
|---------|-------|
| `quality` | Opus ở khắp nơi |
| `balanced` | Opus lập kế hoạch, Sonnet thực thi (mặc định) |
| `budget` | Sonnet viết, Haiku nghiên cứu/xác minh |
| `inherit` | Dùng model phiên hiện tại |

```
/gsd-set-profile budget
```

---

## Lệnh Tiện Ích

| Lệnh | Mô tả |
|------|-------|
| `/gsd-cleanup` | Lưu trữ thư mục giai đoạn đã hoàn thành |
| `/gsd-help` | Hiển thị tài liệu tham khảo lệnh |
| `/gsd-update` | Cập nhật GSD lên phiên bản mới nhất |
| `/gsd-join-discord` | Tham gia cộng đồng Discord GSD |

---

## Cấu Trúc File

```
.planning/
├── PROJECT.md            # Tầm nhìn dự án
├── ROADMAP.md            # Phân chia giai đoạn hiện tại
├── STATE.md              # Bộ nhớ & context dự án
├── RETROSPECTIVE.md      # Nhìn lại (cập nhật mỗi milestone)
├── config.json           # Chế độ workflow & cổng
├── todos/
│   ├── pending/          # Todo đang chờ
│   └── done/             # Todo đã hoàn thành
├── debug/
│   └── resolved/         # Vấn đề đã giải quyết
├── milestones/           # Snapshot đã lưu trữ
├── codebase/             # Bản đồ codebase (brownfield)
│   ├── STACK.md
│   ├── ARCHITECTURE.md
│   ├── STRUCTURE.md
│   ├── CONVENTIONS.md
│   ├── TESTING.md
│   ├── INTEGRATIONS.md
│   └── CONCERNS.md
└── phases/
    ├── 01-foundation/
    │   ├── 01-01-PLAN.md
    │   └── 01-01-SUMMARY.md
    └── 02-core-features/
        ├── 02-01-PLAN.md
        └── 02-01-SUMMARY.md
```

---

## Chế Độ Workflow

**Interactive Mode** — Xác nhận từng quyết định lớn, dừng tại checkpoint

**YOLO Mode** — Tự động phê duyệt hầu hết quyết định, chỉ dừng tại điểm quan trọng

> Thay đổi bất cứ lúc nào bằng cách chỉnh `.planning/config.json`

---

## Workflow Phổ Biến

### Bắt đầu dự án mới
```
/gsd-new-project
/clear
/gsd-plan-phase 1
/clear
/gsd-execute-phase 1
```

### Tiếp tục sau khi nghỉ
```
/gsd-progress
```

### Thêm công việc khẩn cấp giữa milestone
```
/gsd-insert-phase 5 "Sửa lỗi bảo mật nghiêm trọng"
/gsd-plan-phase 5.1
/gsd-execute-phase 5.1
```

### Hoàn thành milestone
```
/gsd-complete-milestone 1.0.0
/clear
/gsd-new-milestone "Tính năng tiếp theo"
```

### Ghi lại ý tưởng trong khi làm việc
```
/gsd-add-todo
/gsd-add-todo Sửa z-index modal
/gsd-check-todos
/gsd-check-todos api
```

### Gỡ lỗi một vấn đề
```
/gsd-debug "form submit lỗi im lặng"
/clear
/gsd-debug   ← tiếp tục từ chỗ dừng
```
