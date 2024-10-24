import math
def tinh_f_x(x):
    phan_tu = -x + math.sqrt(x**2 + 4)
    phan_mau = 7 * math.sqrt(x**4 + 1)
    f_x = phan_tu / phan_mau
    return round(f_x, 2)
x = float(input("Nhập giá trị X: "))
ket_qua = tinh_f_x(x)
print("Giá trị của f(", x, ") là: ", ket_qua)
