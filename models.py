class Phong:
    def __init__(self, ma_phong, ten_phong, gia_co_ban):
        self.ma_phong = ma_phong
        self.ten_phong = ten_phong
        self.gia_co_ban = gia_co_ban
        # Tính đóng gói: __trang_thai là thuộc tính private
        self.__trang_thai = "Trống" 

    # Getter để đọc trạng thái an toàn từ bên ngoài
    def get_trang_thai(self):
        return self.__trang_thai

    # Setter để thay đổi trạng thái hợp lệ thông qua nghiệp vụ
    def set_trang_thai(self, trang_thai_moi):
        if trang_thai_moi in ["Trống", "Đã thuê"]:
            self.__trang_thai = trang_thai_moi

    def tinh_tien(self, so_ngay):
        return self.gia_co_ban * so_ngay

    def to_dict(self):
        return {
            "ma_phong": self.ma_phong,
            "ten_phong": self.ten_phong,
            "gia_co_ban": self.gia_co_ban,
            "trang_thai": self.__trang_thai,
            "loai_phong": "Thuong"
        }


class PhongThuong(Phong):
    def __init__(self, ma_phong, ten_phong, gia_co_ban):
        super().__init__(ma_phong, ten_phong, gia_co_ban)
    
    def tinh_tien(self, so_ngay):
        # Tính đa hình: Phòng thường tính theo công thức cơ bản
        return super().tinh_tien(so_ngay)


class PhongVIP(Phong):
    def __init__(self, ma_phong, ten_phong, gia_co_ban, phi_don_dep, phi_minibar):
        super().__init__(ma_phong, ten_phong, gia_co_ban)
        self.phi_don_dep = phi_don_dep
        self.phi_minibar = phi_minibar

    def tinh_tien(self, so_ngay):
        # Tính đa hình: Tự động cộng các chi phí đặc thù khi gọi trùng tên hàm tinh_tien()
        return super().tinh_tien(so_ngay) + self.phi_don_dep + self.phi_minibar

    def to_dict(self):
        d = super().to_dict()
        d["loai_phong"] = "VIP"
        d["phi_don_dep"] = self.phi_don_dep
        d["phi_minibar"] = self.phi_minibar
        return d


class KhachHang:
    def __init__(self, ma_khach, ten, cccd):
        self.ma_khach = ma_khach
        self.ten = ten
        self.cccd = cccd

    def to_dict(self):
        return {"ma_khach": self.ma_khach, "ten": self.ten, "cccd": self.cccd}


class PhieuThue:
    def __init__(self, khach_hang, phong, so_ngay):
        self.khach_hang = khach_hang  # Nhận vào 1 Object KhachHang
        self.phong = phong            # Nhận vào 1 Object Phong
        self.so_ngay = so_ngay

    def to_dict(self):
        return {
            "khach_hang": self.khach_hang.to_dict(),
            "ma_phong": self.phong.ma_phong,
            "so_ngay": self.so_ngay
        }
