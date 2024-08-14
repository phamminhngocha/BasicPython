#Q5.8
import random  # Nhập thư viện random để tạo số ngẫu nhiên

# Nhập số lượng phần tử của mảng từ người dùng
SoLuongPhanTu = int(input("Nhập số lượng phần tử của mảng: "))

# Khởi tạo một danh sách rỗng để lưu trữ các phần tử của mảng
MangSo = []

# Tạo các phần tử ngẫu nhiên cho mảng
for i in range(SoLuongPhanTu):
    SoNgauNhien = random.randint(1, 100)  # Tạo số ngẫu nhiên từ 1 đến 100
    MangSo.append(SoNgauNhien)  # Thêm số ngẫu nhiên vào danh sách

# In mảng ra màn hình
print("Mảng vừa tạo:", MangSo)

# Tính tổng các phần tử trong mảng
Tong = sum(MangSo)

# Tính giá trị trung bình
GiaTriTrungBinh = Tong / SoLuongPhanTu

# In kết quả ra màn hình
print("Giá trị trung bình của mảng:", GiaTriTrungBinh)
