#Q3.11
'''
Cấu trúc thư mục
MyPackage/
│
├── __init__.py
├── TinhToan.py
└── HienThi.py
Main.py
'''

# Sao lưu code sau ra file TinhToan.py
# Hàm tính tổng hai số
def TinhTong(a, b):
    return a + b

# Sao lưu code sau ra file __init__.py
# Đánh dấu đây là một package


# Sao lưu code sau ra file Main.py
# Import module HienThi từ package
from MyPackage.HienThi import HienThiTong
# Nhập dữ liệu
SoThuNhat = float(input("Nhập số thứ nhất: "))
SoThuHai = float(input("Nhập số thứ hai: "))
# Gọi hàm trong module HienThi
HienThiTong(SoThuNhat, SoThuHai)


# Gợi ý mở rộng: Có thể sử dụng:

# import MyPackage.TinhToan
# Ưu điểm:
# - Dễ nhận biết hàm thuộc module nào.

# from MyPackage.TinhToan import *
# Ưu điểm:
# - Gọi hàm trực tiếp không cần tên module.
# Nhược điểm:
# - Dễ trùng tên hàm khi chương trình lớn.

# import MyPackage.TinhToan as tt
# Ưu điểm:
# - Tên ngắn gọn, dễ sử dụng.
# Ví dụ:
# tt.TinhTong(5, 3)

# Trong package lớn có thể tạo thêm:
# __all__ trong __init__.py
# Ưu điểm:
# - Quản lý các hàm, module được phép import.
