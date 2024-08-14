#Q5.10
import numpy as np

# Nhập kích thước ma trận từ người dùng
SoDong = int(input("Nhập số dòng của ma trận: "))
SoCot = int(input("Nhập số cột của ma trận: "))

# Tạo ma trận toàn số 0 có kích thước m x n
MaTranToanSo0 = np.zeros((SoDong, SoCot), dtype=int)

# In ma trận ra màn hình
print("Ma trận toàn số 0:")
print(MaTranToanSo0)
