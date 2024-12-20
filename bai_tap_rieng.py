
# Khởi tạo danh sách cầu thủ
danh_sach_cau_thu = []

# Hàm hiển thị danh sách cầu thủ
def xem_danh_sach():
    print("\nDanh sách cầu thủ:")
    for cau_thu in danh_sach_cau_thu:
        print(cau_thu)
    if not danh_sach_cau_thu:
        print("Danh sách trống.")

# Hàm nhập thông tin cầu thủ
def nhap_cau_thu():
    try:
        so_luong = int(input("Nhập số lượng cầu thủ cần thêm: "))
        for _ in range(so_luong):
            ma = input("Nhập mã cầu thủ: ")
            ten = input("Nhập tên cầu thủ: ")
            tuoi = int(input("Nhập tuổi cầu thủ: "))
            vi_tri = input("Nhập vị trí (thủ môn/hậu vệ/tiền vệ/tiền đạo): ")
            so_huy_chuong = int(input("Nhập số huy chương: "))
            cau_thu = {
                "ma": ma,
                "ten": ten,
                "tuoi": tuoi,
                "vi_tri": vi_tri,
                "so_huy_chuong": so_huy_chuong
            }
            danh_sach_cau_thu.append(cau_thu)
        print("Đã thêm cầu thủ thành công!")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số cho tuổi và số huy chương!")

# Hàm tính thưởng cho cầu thủ
def tinh_thuong():
    try:
        for cau_thu in danh_sach_cau_thu:
            so_huy_chuong = cau_thu["so_huy_chuong"]
            if so_huy_chuong > 10:
                cau_thu["thuong"] = so_huy_chuong * 500000
            elif 5 <= so_huy_chuong <= 10:
                cau_thu["thuong"] = so_huy_chuong * 300000
            else:
                cau_thu["thuong"] = so_huy_chuong * 200000
        print("Đã tính thưởng cho tất cả cầu thủ.")
    except KeyError as e:
        print(f"Lỗi: Thiếu thông tin quan trọng - {e}")

# Hàm tìm kiếm và xóa cầu thủ theo mã
def xoa_cau_thu():
    try:
        ma = input("Nhập mã cầu thủ cần xóa: ")
        for cau_thu in danh_sach_cau_thu:
            if cau_thu["ma"] == ma:
                danh_sach_cau_thu.remove(cau_thu)
                print(f"Đã xóa cầu thủ có mã {ma}.")
                return
        print("Không tìm thấy cầu thủ cần xóa.")
    except Exception as e:
        print(f"Lỗi xảy ra khi xóa cầu thủ: {e}")

# Hàm tìm kiếm và chỉnh sửa thông tin cầu thủ
def sua_cau_thu():
    try:
        ma = input("Nhập mã cầu thủ cần sửa: ")
        for cau_thu in danh_sach_cau_thu:
            if cau_thu["ma"] == ma:
                print("Nhập thông tin mới:")
                cau_thu["ten"] = input("Nhập tên mới: ")
                cau_thu["tuoi"] = int(input("Nhập tuổi mới: "))
                cau_thu["vi_tri"] = input("Nhập vị trí mới: ")
                cau_thu["so_huy_chuong"] = int(input("Nhập số huy chương mới: "))
                print(f"Đã sửa thông tin cầu thủ có mã {ma}.")
                return