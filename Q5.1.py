#Q5.1
import random  # Nhập thư viện random để tạo các số ngẫu nhiên

# Nhập số lượng phần tử của mảng từ người dùng
SoLuongPhanTu = int(input("Nhập số lượng phần tử của mảng: "))

# Khởi tạo một danh sách rỗng để lưu trữ các phần tử của mảng
Mang = []

# Sử dụng vòng lặp for để thêm các phần tử ngẫu nhiên vào mảng
for i in range(SoLuongPhanTu):
    # Tạo một số ngẫu nhiên từ 1 đến 100 và thêm vào mảng
    PhanTuMoi = random.randint(1, 100)
    Mang.append(PhanTuMoi)

# In ra mảng vừa tạo
print("Mảng vừa tạo là:", Mang)






