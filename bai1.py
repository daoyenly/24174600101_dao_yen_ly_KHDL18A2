def tinh_dien_tich_khoi_tru(ban_kinh, chieu_cao):
    pi = 3.14
    dien_tich_xung_quanh = 2 * pi * ban_kinh * chieu_cao
    dien_tich_toan_phan = 2 * pi * ban_kinh ** 2 + 2 * pi * ban_kinh * chieu_cao

    dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
    dien_tich_toan_phan = round(dien_tich_toan_phan, 2)

    return dien_tich_xung_quanh, dien_tich_toan_phan

ban_kinh = float(input("Nhập bán kính (r): "))
chieu_cao = float(input("Nhập chiều cao (h): "))

dien_tich_xung_quanh, dien_tich_toan_phan = tinh_dien_tich_khoi_tru(ban_kinh, chieu_cao)

print("Diện tích xung quanh của khối trụ là: {}".format(dien_tich_xung_quanh))
print("Diện tích toàn phần của khối trụ là: {}".format(dien_tich_toan_phan))