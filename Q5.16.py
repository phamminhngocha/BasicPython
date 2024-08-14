#Q5.16
import numpy as np

# Nhập kích thước của ma trận vuông
SoDongCot = int(input("Nhập kích thước của ma trận vuông (số dòng = số cột): "))

# Khởi tạo một ma trận rỗng để lưu trữ các phần tử
MaTran = np.zeros((SoDongCot, SoDongCot))

# Nhập các phần tử của ma trận từ bàn phím
print("Nhập các phần tử của ma trận:")
for i in range(SoDongCot):
    for j in range(SoDongCot):
        MaTran[i][j] = float(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))

# Tính định thức của ma trận
DinhThuc = np.linalg.det(MaTran)

# In kết quả
print("Định thức của ma trận là:", DinhThuc)





