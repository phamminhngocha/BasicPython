#Q5.14
import numpy as np

# Nhập kích thước của ma trận
m = int(input("Nhập số dòng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

# Khởi tạo hai ma trận A và B với kích thước m x n
MaTranA = np.zeros((m, n))
MaTranB = np.zeros((m, n))

# Nhập các phần tử của ma trận A
print("Nhập các phần tử của ma trận A:")
for i in range(m):
    for j in range(n):
        MaTranA[i][j] = float(input(f"Nhập phần tử A[{i}][{j}] = "))

# Nhập các phần tử của ma trận B
print("Nhập các phần tử của ma trận B:")
for i in range(m):
    for j in range(n):
        MaTranB[i][j] = float(input(f"Nhập phần tử B[{i}][{j}] = "))

# Tính tổng hai ma trận
MaTranTong = MaTranA + MaTranB

# In kết quả
print("Ma trận A:")
print(MaTranA)
print("Ma trận B:")
print(MaTranB)
print("Ma trận tổng:")
print(MaTranTong)
