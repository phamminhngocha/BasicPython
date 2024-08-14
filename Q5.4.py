#Q5.4
import random  # Nhập thư viện random để tạo số ngẫu nhiên

# Khởi tạo một danh sách rỗng để lưu trữ mảng 2 chiều
Mang2Chieu = []

# Kích thước của mảng
SoHang = 5
SoCot = 5

# Tạo các phần tử ngẫu nhiên và thêm vào mảng
for i in range(SoHang):  # Lặp qua từng hàng
    Hang = []  # Khởi tạo một hàng mới
    for j in range(SoCot):  # Lặp qua từng cột trong hàng
        SoNgauNhien = random.randint(1, 9)  # Tạo số ngẫu nhiên từ 1 đến 9
        Hang.append(SoNgauNhien)  # Thêm số ngẫu nhiên vào hàng
    Mang2Chieu.append(Hang)  # Thêm hàng vào mảng 2 chiều

# In mảng 2 chiều ra màn hình
for Hang in Mang2Chieu:
    print(Hang)
