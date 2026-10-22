from services import QuanLyKhachSan
from models import PhongThuong, PhongVIP, KhachHang

def hien_thi_danh_sach_phong(qlks):
    print("\n--- DANH SÁCH PHÒNG TRONG KHÁCH SẠN ---")
    if not qlks.rooms:
        print("Hệ thống chưa có phòng nào. Hãy thêm phòng mới!")
        return
    for p in qlks.rooms.values():
        loai = "VIP" if isinstance(p, PhongVIP) else "Thường"
        print(f"[{p.ma_phong}] - {p.ten_phong} ({loai}) - Giá gốc: {p.gia_co_ban:,}đ/đêm - Trạng thái: {p.get_trang_thai()}")

def main():
    qlks = QuanLyKhachSan()

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ KHÁCH SẠN =====")
        print("1. Hiển thị danh sách phòng")
        print("2. Thêm phòng mới")
        print("3. Đặt phòng")
        print("4. Trả phòng & Thanh toán")
        print("5. Xem báo cáo doanh thu")
        print("6. Thoát & Lưu dữ liệu")
        
        luat_chon = input("👉 Nhập lựa chọn của bạn (1-6): ").strip()

        if luat_chon == "1":
            hien_thi_danh_sach_phong(qlks)

        elif luat_chon == "2":
            print("\n--- THÊM PHÒNG MỚI ---")
            ma_phong = input("Nhập mã phòng: ").strip()
            ten_phong = input("Nhập tên phòng: ").strip()
            
            # Xử lý ngoại lệ: Chặn lỗi nhập sai định dạng số giá tiền
            try:
                gia_co_ban = float(input("Nhập giá cơ bản (VNĐ): "))
            except ValueError:
                print("❌ Lỗi: Giá phòng phải là một số hợp lệ!")
                continue

            loai = input("Chọn loại phòng (1. Thường / 2. VIP): ").strip()
            if loai == "1":
                phong_moi = PhongThuong(ma_phong, ten_phong, gia_co_ban)
                qlks.them_phong(phong_moi)
            elif loai == "2":
                # Xử lý ngoại lệ: Chặn lỗi nhập chữ tại mục chi phí phụ thu phòng VIP
                try:
                    phi_don_dep = float(input("Nhập phí dọn dẹp: "))
                    phi_minibar = float(input("Nhập phí minibar: "))
                except ValueError:
                    print("❌ Lỗi: Các khoản chi phí phụ thu phải là chữ số!")
                    continue
                phong_moi = PhongVIP(ma_phong, ten_phong, gia_co_ban, phi_don_dep, phi_minibar)
                qlks.them_phong(phong_moi)
            else:
                print("❌ Loại phòng không hợp lệ!")

        elif luat_chon == "3":
            print("\n--- ĐẶT PHÒNG KHÁCH SẠN ---")
            ma_phong = input("Nhập mã phòng khách muốn đặt: ").strip()
            
            # Kiểm tra lỗi nghiệp vụ: Người dùng chọn đặt một phòng không tồn tại trước khi nhập thông tin khách hàng
            if ma_phong not in qlks.rooms:
                print("❌ Lỗi: Mã phòng không tồn tại trên hệ thống!")
                continue
                
            ma_khach = input("Nhập mã khách hàng: ").strip()
            ten_khach = input("Nhập tên khách hàng: ").strip()
            cccd = input("Nhập số CCCD/CMND: ").strip()
            
            # Xử lý ngoại lệ: Nhập chữ tại mục số ngày thuê phòng
            try:
                so_ngay = int(input("Nhập số ngày thuê: "))
                if so_ngay <= 0:
                    print("❌ Số ngày thuê phải lớn hơn 0!")
                    continue
            except ValueError:
                print("❌ Lỗi: Số ngày thuê phải là số nguyên!")
                continue

            khach = KhachHang(ma_khach, ten_khach, cccd)
            qlks.dat_phong(ma_phong, khach, so_ngay)

        elif luat_chon == "4":
            print("\n--- TRẢ PHÒNG & THANH TOÁN ---")
            ma_phong = input("Nhập mã phòng cần trả: ").strip()
            qlks.tra_phong(ma_phong)

        elif luat_chon == "5":
            qlks.bao_cao_doanh_thu()

        elif luat_chon == "6":
            qlks.luu_tat_ca_du_lieu()
            print("👋 Cảm ơn bạn đã sử dụng hệ thống quản lý. Hẹn gặp lại!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng nhập chính xác từ 1 đến 6.")

if __name__ == "__main__":
    main()
