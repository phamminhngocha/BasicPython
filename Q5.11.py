#Q5.11
import random

# Nhập giá trị m từ người dùng
m = int(input("Nhập số nguyên dương m: "))

# Tạo mảng một chiều có 2m phần tử với các giá trị ngẫu nhiên từ 1 đến 100
MangMotChieu = [random.randint(1, 100) for _ in range(2*m)]
print("Mảng một chiều:", MangMotChieu)

# Tạo mảng hai chiều có kích thước 2 dòng, m cột từ mảng một chiều
MangHaiChieu = []
for i in range(2):
    # Tạo một hàng mới cho mảng hai chiều
    HangMoi = MangMotChieu[i*m:(i+1)*m]
    MangHaiChieu.append(HangMoi)

# In mảng hai chiều
print("Mảng hai chiều:")
for Hang in MangHaiChieu:
    print(Hang)
