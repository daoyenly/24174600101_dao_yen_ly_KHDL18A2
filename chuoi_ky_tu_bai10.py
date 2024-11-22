input_string = input("Nhập vào chuỗi ký tự: ")

chu_so = ''.join(char for char in input_string if char.isdigit())  
chu_cai = ''.join(char for char in input_string if not char.isdigit())

cong_tong = chu_so + chu_cai  
print(f"Chuỗi mới sau khi dồn số sang bên trái: {cong_tong}")