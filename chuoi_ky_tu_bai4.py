input_string = input("Nhap chuoi ky tu: ")

chu_ky_tu = 0
so_ky_tu = 0
so_ky_tu_dac_biet = 0

for char in input_string:
    if char.isalpha():
        chu_ky_tu += 1
    elif char.isdigit():
        so_ky_tu += 1
    else:
        so_ky_tu_dac_biet += 1

print(f"Chu_cai: {chu_ky_tu}, So: {so_ky_tu}, Ky_tu_dac_biet: {so_ky_tu_dac_biet}") 