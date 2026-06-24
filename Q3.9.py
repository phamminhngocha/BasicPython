# Q3.9
'''
Cấu trúc thư mục
TinhToan/
│
├── __init__.py
├── PhepTinh.py
├── HinhChuNhat.py
│
└── Main.py
'''

# Sao chép code sau ra file PhepTinh.py
# Module thực hiện các phép tính cơ bản
def Cong(a, b):
    return a + b
def Nhan(a, b):
    return a * b

# Sao chép code sau ra file HinhChuNhat.py
# Import các hàm từ module khác trong cùng package
from TinhToan.PhepTinh import Cong
from TinhToan.PhepTinh import Nhan
def ChuVi(ChieuDai, ChieuRong):
    TongHaiCanh = Cong(ChieuDai, ChieuRong)
    return Nhan(TongHaiCanh, 2)
def DienTich(ChieuDai, ChieuRong):
    return Nhan(ChieuDai, ChieuRong)

# Sao chép code sau ra file __init__.py
# Đánh dấu thư mục là một package

# Sao chép code sau ra file Main.py
# Sử dụng các chức năng từ module con trong package
from TinhToan.HinhChuNhat import ChuVi
from TinhToan.HinhChuNhat import DienTich
ChieuDai = float(input("Nhập chiều dài: "))
ChieuRong = float(input("Nhập chiều rộng: "))
KetQuaChuVi = ChuVi(ChieuDai, ChieuRong)
KetQuaDienTich = DienTich(ChieuDai, ChieuRong)
print("Chu vi hình chữ nhật =", KetQuaChuVi)
print("Diện tích hình chữ nhật =", KetQuaDienTich)

# Gợi ý:
# - Có thể sử dụng cú pháp:
#   import TinhToan.HinhChuNhat
#   để gọi:
#   TinhToan.HinhChuNhat.ChuVi(...)

# - Có thể sử dụng:
#   from TinhToan.HinhChuNhat import *
#   để nhập toàn bộ hàm trong module.

# - Có thể sử dụng package nhiều tầng (subpackage)
#   khi dự án lớn.

# Điểm tốt của cách hiện tại:
# - Mã nguồn dễ bảo trì.
# - Module HinhChuNhat tái sử dụng được module PhepTinh.
# - Chương trình chính chỉ cần gọi các hàm cần thiết.
# - Tăng tính đóng gói và khả năng mở rộng của dự án.

