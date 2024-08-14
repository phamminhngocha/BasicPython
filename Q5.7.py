#Q5.7
# Nhập số lượng phần tử của mảng từ người dùng
SoLuongPhanTu = int(input("Nhập số lượng phần tử của mảng: "))

# Khởi tạo một danh sách rỗng để lưu trữ các phần tử của mảng
MangSo = []

# Nhập từng phần tử của mảng từ người dùng và thêm vào danh sách
for i in range(SoLuongPhanTu):
    So1 = int(input(f"Nhập phần tử thứ {i+1}: "))
    MangSo.append(So1)

# Khởi tạo biến để lưu tổng các số lẻ
TongSoLe = 0

# Duyệt qua từng phần tử trong mảng
for So2 in MangSo:
    # Kiểm tra xem số đó có phải là số lẻ không
    if So2 % 2 != 0:
        # Nếu là số lẻ, cộng vào tổng các số lẻ
        TongSoLe += So2

# In ra kết quả
print("Tổng các số lẻ trong mảng là:", TongSoLe)
