from models import PhongThuong, PhongVIP, KhachHang, PhieuThue
import file_handler

class QuanLyKhachSan:
    def __init__(self):
        # Tự động nạp bộ nhớ lưu trữ từ file dữ liệu cũ lên RAM khi khởi chạy lớp dịch vụ
        self.rooms, self.phieu_thues, self.total_revenue = file_handler.load_data()

    def them_phong(self, phong):
        """Thêm phòng mới và chặn trùng lặp mã phòng"""
        if phong.ma_phong in self.rooms:
            print(f"❌ Lỗi: Mã phòng {phong.ma_phong} đã tồn tại trong hệ thống!")
            return False
        self.rooms[phong.ma_phong] = phong
        print(f"✅ Thêm phòng {phong.ten_phong} thành công.")
        return True

    def dat_phong(self, ma_phong, khach_hang, so_ngay):
        """Xử lý nghiệp vụ đặt phòng và chuyển trạng thái phòng"""
        if ma_phong not in self.rooms:
            print("❌ Lỗi: Mã phòng không tồn tại trong hệ thống!")
            return

        phong = self.rooms[ma_phong]
        if phong.get_trang_thai() == "Đã thuê":
            print(f"❌ Lỗi: Phòng {ma_phong} hiện tại đang có khách ở!")
            return

        # Thực thi chuyển đổi trạng thái bằng phương thức nghiệp vụ hợp lệ
        phong.set_trang_thai("Đã thuê")
        new_phieu = PhieuThue(khach_hang, phong, so_ngay)
        self.phieu_thues[ma_phong] = new_phieu
        print(f"🎉 Đặt phòng {ma_phong} thành công cho khách hàng {khach_hang.ten}!")

    def tra_phong(self, ma_phong):
        """Xử lý tính hóa đơn theo Đa hình, giải phóng phòng và lưu doanh thu lịch sử"""
        if ma_phong not in self.rooms:
            print("❌ Lỗi: Mã phòng không tồn tại!")
            return

        phong = self.rooms[ma_phong]
        if phong.get_trang_thai() == "Trống":
            print(f"❌ Lỗi: Phòng {ma_phong} đang trống, không thể thực hiện trả!")
            return

        phieu = self.phieu_thues.get(ma_phong)
        if phieu:
            # Tính đa hình: Hệ thống tự gọi hàm tinh_tien của PhongThuong hoặc PhongVIP 
            # dựa trên bản chất thật của Object đang trỏ tới mà không cần viết lệnh if-else phức tạp.
            thanh_tien = phong.tinh_tien(phieu.so_ngay)
            self.total_revenue += thanh_tien
            
            # Chuyển trạng thái phòng về trống và xóa phiếu thuê khỏi danh sách đang hoạt động
            phong.set_trang_thai("Trống")
            del self.phieu_thues[ma_phong]
            
            print(f"💳 TRẢ PHÒNG {ma_phong} THÀNH CÔNG!")
            print(f"   Khách hàng: {phieu.khach_hang.ten}")
            print(f"   Số ngày ở: {phieu.so_ngay}")
            print(f"   Tổng tiền thanh toán: {thanh_tien:,} VNĐ")

    def bao_cao_doanh_thu(self):
        """Tính toán thống kê doanh thu và phòng trống hiện tại"""
        phong_trong = sum(1 for p in self.rooms.values() if p.get_trang_thai() == "Trống")
        print("\n================ BÁO CÁO DOANH THU ================")
        print(f"📈 Tổng doanh thu tích lũy: {self.total_revenue:,} VNĐ")
        print(f"🚪 Số lượng phòng hiện đang trống: {phong_trong} / {len(self.rooms)}")
        print("===================================================")

    def luu_tat_ca_du_lieu(self):
        """Gửi lệnh cập nhật dữ liệu xuống module xử lý file"""
        file_handler.save_data(self.rooms, self.phieu_thues, self.total_revenue)
        print("💾 Đã lưu dữ liệu vào hệ thống an toàn.")
