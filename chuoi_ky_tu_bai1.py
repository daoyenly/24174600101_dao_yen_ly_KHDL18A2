input_string = input("Nhap chuoi ky tu: ")

input_string = input_string.strip()

danh_sach = input_string.split()

dem_so_chuoi = len(danh_sach)

print(f"So tu trong chuoi la: {dem_so_chuoi}")