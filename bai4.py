hieu_dien_the = 220
cuong_do_dong_dien = 2.7
gia_dien = 7000

thoi_gian_su_dung = float(input("Thời gian sử dụng bóng điện(s): "))

cong_suat_tieu_thu = hieu_dien_the * cuong_do_dong_dien

thoi_gian_gio = thoi_gian_su_dung / 3600
dien_nang_tieu_thu = (cong_suat_tieu_thu / 1000) * thoi_gian_gio

tinh_gia_tien = dien_nang_tieu_thu * gia_dien

print("Điện năng tiêu thụ là: ", round(dien_nang_tieu_thu, 2), "kwh")
print("Giá điện là: ", round(tinh_gia_tien, 2), "Đồng")