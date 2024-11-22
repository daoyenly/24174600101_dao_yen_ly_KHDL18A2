input_string = input("Nhap vao mot chuoi ky tu nhi phan: ")

if all(char in '01' for char in input_string):  
    print(f"'{input_string}' là số nhị phân.")  
     
    decimal_num = int(input_string, 2)  
    print(f"Chuyển sang số thập phân: {decimal_num}")  
else:  
    print(f"'{input_string}' không phải là số nhị phân.")