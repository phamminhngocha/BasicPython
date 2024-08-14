#Q2.24

import math

# Nhập lựa chọn của người dùng
print("Chọn cách tính diện tích tam giác:")
print("1. Bằng 3 cạnh")
print("2. Bằng 1 cạnh và chiều cao")
print("3. Bằng 2 cạnh và góc xen giữa")
Chon = int(input("Nhập lựa chọn của bạn: "))

# Tính diện tích theo lựa chọn
if Chon == 1:
    # Nhập độ dài 3 cạnh
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))

    # Kiểm tra điều kiện tồn tại tam giác
    if a + b > c and a + c > b and b + c > a and a>0 and b>0 and c>0:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Diện tích tam giác là:", S)
    else:
        print("Ba cạnh không tạo thành một tam giác.")
elif Chon == 2:
    # Nhập độ dài cạnh đáy và chiều cao
    Day = float(input("Nhập độ dài cạnh đáy: "))
    ChieuCao = float(input("Nhập chiều cao tương ứng: "))
    # Kiểm tra điều kiện cạnh và chiều cao dương
    if Day > 0 and ChieuCao > 0:
        S = Day * ChieuCao/2
        print("Diện tích tam giác là:", S)
    else:
        print("Độ dài cạnh đáy và chiều cao phải là số dương.")
elif Chon == 3:
    # Nhập độ dài 2 cạnh và góc xen giữa
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    Goc = float(input("Nhập góc xen giữa (độ): "))
    # Kiểm tra điều kiện cạnh dương và góc trong khoảng 0 đến 180 độ
    if a > 0 and b > 0 and 0 < Goc < 180:
        S = a * b * math.sin(math.radians(Goc))/2
        print("Diện tích tam giác là:", S)
    else:
        print("Độ dài cạnh phải dương và góc phải nằm trong khoảng 0 đến 180 độ.")
else:
    print("Lựa chọn không hợp lệ.")
