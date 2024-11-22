input_string = input("Nhap chuoi ky tu: ")

chu_viet_hoa = 0
chu_viet_thuong = 0

for char in input_string:
    if char.isupper():
        chu_viet_hoa += 1
    elif char.islower():
        chu_viet_thuong += 1

print(f"So chu cai viet hoa: {chu_viet_hoa}")
print(f"So chu cai viet thuong: {chu_viet_thuong}")