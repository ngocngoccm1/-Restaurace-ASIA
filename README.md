# Restaurace ASIA — website cho GitHub Pages

Website tĩnh hoàn chỉnh nằm **ngay thư mục gốc**:

- `index.html`: homepage với chữ lớn, ảnh món trong khung vòm và bố cục biên tập, nội dung/ảnh Restaurace ASIA.
- `menu.html`: menu đọc với ảnh bên cạnh từng món, không có giỏ hàng hay thanh toán.
- `styles.css`, `app.js`, `assets/`, `fonts/`, `data/`: tài nguyên website.
- `.nojekyll`: cho GitHub Pages phục vụ trực tiếp các file tĩnh.

## Host bằng GitHub Pages

Đưa các file/thư mục trên vào root của repository. Trong **Settings → Pages**, chọn **Deploy from a branch**, branch chứa website và **/(root)**. Không cần npm, build hay backend. Đường dẫn tương đối hoạt động cả với `username.github.io/repository/` và custom domain.

`restaurace-asia-github-pages.zip` chứa sẵn bộ website để upload; `index.html` nằm ngay bên trong root của ZIP. Không cần upload `research/`, tài liệu Word, ảnh nguồn ngoài thư mục assets hay thư mục `website/` cũ.

## Xem và cập nhật

Xem nhanh bằng cách mở `index.html`, hoặc chạy `python3 -m http.server 5173` tại thư mục này rồi mở http://localhost:5173/.

Tên món, giá và biến thể được giữ trong `data/menu.json`. Sau khi sửa dữ liệu, chạy `python3 scripts/build-menu.py` để cập nhật HTML tĩnh. Không có lựa chọn biến thể trên giao diện; mọi giá được liệt kê để khách đọc. Bản ảnh menu gốc đủ 8 trang, bao gồm trang cuối được cung cấp riêng, nằm ở `assets/menu-restaurace-asia.pdf`.

Thông tin liên hệ/giờ mở cửa chỉnh trong `index.html` và đoạn header/footer của script nếu cần. Sau khi sửa homepage, có thể chạy lại script để đồng bộ header/footer của menu.

`website/` và `asia-site.tar.gz` giữ phiên bản trước. Bản mới trong root dùng cho GitHub Pages; không phụ thuộc deployment trước đó.

Nguồn ảnh: `ASSET_SOURCES.json`. Những dữ liệu cần chủ quán xác nhận: `CONTENT_REVIEW.md`. Phân tích reference và mapping: `DESIGN_REFERENCE.md`.

Bản thiết kế mới dùng Bricolage Grotesque + Manrope hỗ trợ tiếng Séc, ảnh thật và các mảng xanh–kem–sage–gỗ. Đã kiểm tra cả homepage/menu ở 375, 390, 430, 768, 1440 và 1920px. Chi tiết: `QA_REPORT.md`.

## Cập nhật ảnh, menu và phòng nghỉ — 25/10/2026

- Mục ubytování: 6 ảnh thật do chủ quán gửi, video MP4 xem trực tiếp, thông tin căn hộ 40 m² / 4 giường, bếp, phòng tắm và WC chung, bữa sáng, giá 750 / 650 / 550 Kč.
- Mỗi món trong 45 mục menu có ảnh bên cạnh; 43 ảnh AI minh họa được ghi rõ, 2 ảnh thật của nhà hàng được giữ lại. Ảnh tối ưu WebP, lưu cục bộ trong `assets/dishes/`. Prompt và công cụ tạo ảnh nằm trong `data/food-image-prompts.json`.
- File gốc `index.html` và mọi tài nguyên dùng đường dẫn tương đối, không cần build khi đưa lên GitHub Pages.
