#Q5.12
import numpy as np

# Nhập kích thước ma trận từ người dùng
SoDong = int(input("Nhập số dòng của ma trận: "))
SoCot = int(input("Nhập số cột của ma trận: "))

# Tạo ma trận toàn số 1 có kích thước đã nhập
MaTranToanMot = np.ones((SoDong, SoCot), dtype=int)

# In ma trận ra màn hình
print(MaTranToanMot)
