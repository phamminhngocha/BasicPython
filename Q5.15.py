#Q5.15
import random

# Nhập kích thước ma trận từ người dùng
SoDong = int(input("Nhập số dòng của ma trận: "))
SoCot = int(input("Nhập số cột của ma trận: "))

# Khởi tạo ma trận ngẫu nhiên
MaTran = []
for i in range(SoDong):
    Row = []
    for j in range(SoCot):
        # Tạo số ngẫu nhiên từ 1 đến 10
        SoNgauNhien = random.randint(1, 10)
        Row.append(SoNgauNhien)
    MaTran.append(Row)

# In ma trận ban đầu
print("Ma trận ban đầu:")
for Row in MaTran:
    print(Row)

# Nhập số nguyên cần cộng
SoCanCong = int(input("Nhập số nguyên cần cộng vào ma trận: "))

# Cộng từng phần tử của ma trận với số nguyên
for i in range(SoDong):
    for j in range(SoCot):
        MaTran[i][j] += SoCanCong

# In ma trận sau khi cộng
print("Ma trận sau khi cộng:", SoCanCong)
for Row in MaTran:
    print(Row)
