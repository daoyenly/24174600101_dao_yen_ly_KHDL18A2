input_string = input("Nhap chuoi ky tu: ")

if input_string.replace('.', '', 1).isdigit():
    print(f"Day '{input_string}' la so thap phan")
else:
    print(f"Day '{input_string}' ko phai so thap phan")