#Q3.7
'''
Cấu trúc thư mục
MyPackage/
│
├── __init__.py
├── TinhToan.py
└── HienThi.py
'''
# Copy code sau ra file MyPackage/TinhToan.py
# Module chứa các hàm tính toán
def Tong(a, b):
    # Trả về tổng của hai số
    return a + b
def Hieu(a, b):
    # Trả về hiệu của hai số
    return a - b

# Copy code sau ra file MyPackage/HienThi.py
# Module chứa các hàm hiển thị
def Chao():
    # Hiển thị lời chào
    print("Xin chao tu package MyPackage")

# Copy code sau ra file MyPackage/__init__.py
# Đánh dấu thư mục MyPackage là một package
print("MyPackage da duoc nap")

# Copy code sau ra file Main.py
# Nhập module TinhToan từ package MyPackage
from MyPackage import TinhToan
# Nhập module HienThi từ package MyPackage
from MyPackage import HienThi
# Gọi hàm trong module HienThi
HienThi.Chao()
# Nhập dữ liệu từ bàn phím
a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
# Gọi hàm trong module TinhToan
TongHaiSo = TinhToan.Tong(a, b)
HieuHaiSo = TinhToan.Hieu(a, b)

# Hiển thị kết quả
print("Tong =", TongHaiSo)
print("Hieu =", HieuHaiSo)


# Có thể sử dụng:
# import MyPackage.TinhToan
# Ưu điểm:
# - Thể hiện rõ module thuộc package nào.

# from MyPackage.TinhToan import Tong, Hieu
# Ưu điểm:
# - Gọi trực tiếp Tong(a,b), Hieu(a,b)
# - Code ngắn gọn hơn.

# from MyPackage import *
# Ưu điểm:
# - Truy cập nhanh các module đã khai báo trong __init__.py
# Nhược điểm:
# - Dễ gây trùng tên biến hoặc hàm.
