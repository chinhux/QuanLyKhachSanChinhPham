import json
import os
from models import PhongThuong, PhongVIP

FILE_PATH = "khachsan_data.json"

def save_data(danh_sach_phong, danh_sach_phieu, doanh_thu_lich_su):
    """Xuất toàn bộ dữ liệu ra file JSON khi người dùng chọn thoát"""
    data = {
        "phong": [p.to_dict() for p in danh_sach_phong.values()],
        "phieu_thue": [p.to_dict() for p in danh_sach_phieu.values()],
        "doanh_thu_lich_su": doanh_thu_lich_su
    }
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_data():
    """Tự động khôi phục dữ liệu từ file JSON khi khởi động hệ thống"""
    # Xử lý ngoại lệ: Nếu file chưa từng tồn tại, trả về cấu trúc rỗng ban đầu thay vì báo lỗi
    if not os.path.exists(FILE_PATH):
        return {}, {}, 0

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        phong_dict = {}
        phieu_dict = {}
        doanh_thu_lich_su = data.get("doanh_thu_lich_su", 0)

        # Khôi phục danh sách các phòng
        for p in data.get("phong", []):
            if p["loai_phong"] == "Thuong":
                obj = PhongThuong(p["ma_phong"], p["ten_phong"], p["gia_co_ban"])
            else:
                obj = PhongVIP(p["ma_phong"], p["ten_phong"], p["gia_co_ban"], p["phi_don_dep"], p["phi_minibar"])
            obj.set_trang_thai(p["trang_thai"])
            phong_dict[p["ma_phong"]] = obj

        # Khôi phục danh sách phiếu thuê hiện tại
        from models import KhachHang, PhieuThue
        for pt in data.get("phieu_thue", []):
            kh = KhachHang(pt["khach_hang"]["ma_khach"], pt["khach_hang"]["ten"], pt["khach_hang"]["cccd"])
            phong_obj = phong_dict.get(pt["ma_phong"])
            if phong_obj:
                phieu_obj = PhieuThue(kh, phong_obj, pt["so_ngay"])
                phieu_dict[phong_obj.ma_phong] = phieu_obj

        return phong_dict, phieu_dict, doanh_thu_lich_su
    except Exception:
        # Dự phòng trường hợp file JSON lỗi định dạng do chỉnh sửa thủ công bên ngoài
        return {}, {}, 0
