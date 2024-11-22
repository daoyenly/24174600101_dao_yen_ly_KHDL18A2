input_string = input("Nhap chuoi ky tu: ")

if input_string.startswith("-") and input_string[1:].isdigit:
    input(f"Day '{input_string}' la so am ")
elif input_string.isdigit():
    input(f"Day '{input_string}' ko phai la so am ")
else:
    input(f"Chuoi '{input_string}' ky tu ko phai la so ")