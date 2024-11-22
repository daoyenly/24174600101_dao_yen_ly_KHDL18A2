nhap_ho_ten = input("Nhap Ho va Ten : ")

danh_sach = nhap_ho_ten.split()

last_name = danh_sach[0]
first_name = danh_sach[-1]

print(f"Ho: '{last_name}', Ten: '{first_name}'")