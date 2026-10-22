
HỆ THỐNG QUẢN LÝ KHÁCH SẠN (CLI APPLICATION) by Chinh Pham

Tài liệu này hướng dẫn chi tiết cách cài đặt môi trường, cấu hình biến PATH, khởi chạy dự án trên Visual Studio Code và các bước kiểm thử hệ thống nhằm đáp ứng các tiêu chí chấm điểm của môn học.

PHẦN 1: HƯỚNG DẪN CÀI ĐẶT & KHỞI CHẠY DỰ ÁN
1. Cài đặt Python và Quản lý môi trường (bằng UV)

Dự án sử dụng trình quản lý gói hiện đại uv để tự động cài đặt phiên bản Python ổn định cao mà không làm ảnh hưởng đến các phiên bản cũ trên máy tính của bạn.
1. Mở PowerShell trên Windows: Bấm phím Windows, gõ PowerShell, chuột phải chọn Run as Administrator.
2. Cài đặt công cụ UV: Copy lệnh sau dán vào và nhấn Enter:powershell
irm https://astral.sh | iex
Hãy thận trọng khi sử dụng mã.
3. Cài đặt Python 3.15.1: Gõ tiếp lệnh sau để cài đặt phiên bản Python mới nhất:powershell
uv python install
Hãy thận trọng khi sử dụng mã.

2. Cấu hình biến môi trường PATH (Sửa triệt để lỗi "Python not found")

Sau khi cài đặt xong, bạn cần cấu hình cố định đường dẫn để hệ thống Windows nhận diện lệnh chạy:
1. Chạy lệnh cập nhật cấu hình shell tự động:powershell
uv python update-shell
Hãy thận trọng khi sử dụng mã.
2. Khởi động lại máy tính hoặc Tắt hoàn toàn VS Code đi rồi mở lại để cấu hình chính thức có hiệu lực.

3. Mở và Khởi chạy dự án trên VS Code

1. Mở phần mềm VS Code.
2. Chọn File > Open Folder... > Tìm và chọn đúng thư mục QuanLyKhachSanChinhPham.
3. Mở Terminal tích hợp của VS Code bằng tổ hợp phím: Ctrl + ~ (hoặc chọn Terminal > New Terminal ở thanh menu trên cùng).
4. Khởi chạy ứng dụng bằng công cụ uv với lệnh:
powershell
uv run main.py

PHẦN 2: KỊCH BẢN KIỂM THỬ ĐÁP ỨNG CÁC YÊU CẦU ĐỀ BÀI
Lưu ý trước khi test: Để chạy thử nghiệm hệ thống từ trạng thái sạch ban đầu, hãy xóa file khachsan_data.json trong thư mục dự án (nếu có).

Yêu cầu 1 & 5: Kiểm thử Xử lý ngoại lệ (Exception Handling)

Mục tiêu: Đảm bảo ứng dụng không bao giờ bị crash (văng lỗi đỏ) khi người dùng nhập sai định dạng.
• Kịch bản 1: Nhập chữ vào ô yêu cầu nhập số (Giá tiền/Phí phụ thu)
	• Hành động: Tại Menu chính, nhập 2 để Thêm phòng mới.
	• Thao tác nhập: Mã phòng: 101 | Tên: Phong Standard | Giá cơ bản: Cố tình nhập chuỗi chữ abc hoặc năm trăm nghìn.
	• Kết quả kỳ vọng: Hệ thống phát hiện lỗi định dạng, in ra thông báo: ❌ Lỗi: Giá phòng phải là một số hợp lệ! và tự động đưa người dùng quay lại Menu chính an toàn.
• Kịch bản 2: Đặt một phòng không tồn tại
	• Hành động: Tại Menu chính, nhập 3 để Đặt phòng.
	• Thao tác nhập: Nhập mã phòng khách muốn đặt: 999 (Mã phòng chưa từng được tạo).
	• Kết quả kỳ vọng: Hệ thống chặn ngay lập tức, báo lỗi: ❌ Lỗi: Mã phòng không tồn tại trên hệ thống! và không yêu cầu nhập tiếp thông tin khách hàng, tránh lãng phí thời gian thao tác.
• Kịch bản 3: Nhập sai định dạng số ngày thuê phòng
	• Thao tác chuẩn bị: Vào chức năng 2 -> Thêm phòng 101 hợp lệ (Giá: 500000, Loại: 1).
	• Hành động: Vào chức năng 3 -> Nhập mã phòng: 101 -> Nhập thông tin khách tùy ý.
	• Thao tác nhập lỗi: Tại dòng "Nhập số ngày thuê", cố tình nhập chữ xyz hoặc số âm -5.
	• Kết quả kỳ vọng: Hệ thống báo lỗi tương ứng (Số ngày thuê phải là số nguyên! hoặc Số ngày thuê phải lớn hơn 0!) và đưa về Menu mà không đổi trạng thái phòng.

Yêu cầu 1 & 2: Kiểm thử Tính đóng gói, Kế thừa & Nghiệp vụ đặt phòng

Mục tiêu: Đảm bảo dữ liệu phòng được phân cấp chính xác và trạng thái phòng được bảo vệ nghiêm ngặt.
• Hành động 1: Thêm phòng Thường (Lớp con PhongThuong)
	• Chọn 2 -> Nhập mã: 101 -> Tên: Standard Room -> Giá: 500000 -> Chọn loại phòng: 1.
• Hành động 2: Thêm phòng VIP (Lớp con PhongVIP có thuộc tính chi phí riêng)
	• Chọn 2 -> Nhập mã: 201 -> Tên: VIP Suite -> Giá: 1200000 -> Chọn loại phòng: 2 -> Phí dọn dẹp: 100000 -> Phí minibar: 150000.
• Hành động 3: Xem danh sách để kiểm tra nghiệp vụ và Đóng gói
	• Chọn chức năng số 1.
	• Kết quả kỳ vọng: Hệ thống in ra danh sách 2 phòng vừa tạo. Thuộc tính ẩn danh __trang_thai (private) của các phòng được hiển thị chính xác là Trống thông qua hàm bảo mật get_trang_thai().

Yêu cầu 2 & 4: Kiểm thử Tính Đa hình (Polymorphism) & Trả phòng

Mục tiêu: Xác thực tính đa hình khi hệ thống tự động áp dụng công thức tính tiền khác nhau tùy theo loại phòng thực tế.
• Hành động 1: Đặt phòng cho khách
	• Vào chức năng 3 -> Đặt phòng 101 với số ngày thuê là 2 ngày.
	• Vào chức năng 3 -> Đặt phòng 201 với số ngày thuê là 2 ngày.
• Hành động 2: Trả phòng Thường (101)
	• Chọn chức năng số 4 -> Nhập mã phòng: 101.
	• Kết quả kỳ vọng: Tổng tiền hiển thị chính xác theo công thức phòng thường: 500.000 * 2 = 1.000.000 VNĐ.
• Hành động 3: Trả phòng VIP (201) - Chứng minh tính Đa hình
	• Chọn chức năng số 4 -> Nhập mã phòng: 201.
	• Kết quả kỳ vọng: Hệ thống tự động kích hoạt hàm tinh_tien() nạp chồng riêng của lớp PhongVIP để cộng thêm các khoản phụ thu mà không cần viết các câu lệnh rẽ nhánh rườm rà.
	• Công thức: (1.200.000 * 2) + 100.000 (Dọn dẹp) + 150.000 (Minibar) = 2.650.000 VNĐ.

Yêu cầu 3 & 4: Kiểm thử Báo cáo & Lưu trữ file dữ liệu JSON

Mục tiêu: Đảm bảo chức năng thống kê chính xác và cơ chế nạp/xuất dữ liệu không bị mất mát khi tắt ứng dụng.
• Hành động 1: Kiểm tra báo cáo tổng hợp
	• Chọn chức năng số 5 trên Menu.
	• Kết quả kỳ vọng: Tổng doanh thu tích lũy hiển thị chính xác: 3.650.000 VNĐ (bằng tổng tiền 2 phòng đã trả ở trên). Số lượng phòng hiện đang trống báo cáo: 2 / 2.
• Hành động 2: Đặt lại một phòng và Thoát lưu dữ liệu
	• Chọn 3 -> Tiến hành đặt lại phòng 101 với số ngày ở là 3 ngày để phòng này chuyển sang trạng thái Đã thuê.
	• Chọn chức năng số 6 để Thoát & Lưu dữ liệu. Hệ thống sẽ tự đóng.
• Hành động 3: Xác thực khả năng lưu trữ file và khôi phục (Load Data)
	• Mở cây thư mục bên trái VS Code, bạn sẽ thấy xuất hiện tệp khachsan_data.json chứa dữ liệu đã mã hóa.
	• Chạy lại ứng dụng bằng lệnh: uv run main.py.
	• Chọn chức năng số 1 (Hiển thị danh sách phòng) và chức năng số 5 (Báo cáo doanh thu).
	• Kết quả kỳ vọng: Toàn bộ lịch sử được khôi phục hoàn hảo: Phòng 101 vẫn giữ nguyên trạng thái Đã thuê, phòng 201 giữ trạng thái Trống, và tổng số tiền doanh thu cũ 3.650.000 VNĐ vẫn được lưu giữ trọn vẹn trong bộ nhớ.
