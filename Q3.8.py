# Q3.8
'''
Giả sử ở câu 3.7 đã tạo package MyPackage. 
Nay mở rộng thêm subpackage TinhToan và sử dụng module Cong.py từ subpackage trong chương trình chính.
Cấu trúc thư mục:
MyPackage/
│
├── __init__.py
│
└── TinhToan/
    ├── __init__.py
    └── Cong.py
Main.py
'''

# Sao chép code sau ra file MyPackage/TinhToan/Cong.py
# Hàm thực hiện phép cộng hai số
def cong(a, b):
    return a + b

# Sao chép code sau ra file Main.py
# Import hàm cong từ module Cong thuộc subpackage TinhToan
from MyPackage.TinhToan.Cong import cong
# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
# Gọi hàm cong trong module Cong
ket_qua = cong(a, b)
# Hiển thị kết quả
print("Tổng =", ket_qua)

# Gợi ý một số cách khác:

# from MyPackage.TinhToan import Cong
# Ưu điểm: Truy cập được toàn bộ nội dung module Cong.

# import MyPackage.TinhToan.Cong
# Ưu điểm: Thể hiện rõ đường dẫn package và subpackage.

# from MyPackage.TinhToan.Cong import *
# Ưu điểm: Gọi trực tiếp tên hàm.
# Nhược điểm: Dễ gây trùng tên hàm trong chương trình lớn.

# Nên sử dụng:
# from MyPackage.TinhToan.Cong import cong
# vì ngắn gọn, dễ đọc và chỉ import đúng hàm cần dùng.
