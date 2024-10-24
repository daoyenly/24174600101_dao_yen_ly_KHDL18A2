import math
def tinh_f(x):
    log_4_x = math.log(x, 4)
    log_x_2 = math.log(2, x)
    f_x = log_4_x + log_x_2
    return f_x 
x = float(input("Nhập x (x > 0): "))

if x <= 0:
    print("Phải nhập gia trị x lớn hơn 0")
else:
    ket_qua = tinh_f(x)
    print(f"Giá trị của f(x) là: {round(ket_qua, 2)}")
