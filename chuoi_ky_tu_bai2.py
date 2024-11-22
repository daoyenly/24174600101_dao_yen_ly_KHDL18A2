input_string = input("Nhap chuoi ky tu: ")

danh_sach = input_string.split()

xoa_khoang_trang = ' '.join(danh_sach)

print(f"Chuoi ky tu sau khi bi loai bo la: {xoa_khoang_trang}")