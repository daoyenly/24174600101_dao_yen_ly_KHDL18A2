str_1 = input("Nhap chuoi ky tu: ")
str_2 = input("Nhap chuoi ky tu: ")

if str_2 in str_1:
    print(f"{str_2} nam trong {str_1}.")
else:
    print(f"{str_2} ko nam trong {str_1}.")
# kiem tra lai
if str_1 in str_2:
    print(f"{str_1} nam trong {str_2}.")
else:
    print(f"{str_1} ko nam trong {str_2}.")