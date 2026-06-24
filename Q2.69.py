#Q2.69
# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử n = "))

# Khởi tạo danh sách rỗng
DanhSach = []

# Nhập các phần tử và đưa vào danh sách
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    DanhSach.append(x)  # Thêm phần tử x vào cuối danh sách

# Khởi tạo biến lưu tổng
Tong = 0

# Duyệt từng phần tử trong danh sách
for x in DanhSach:
    # Kiểm tra phần tử có chia hết cho 5 hay không
    if x % 5 == 0:
        Tong += x  # Cộng giá trị x vào tổng

# Hiển thị kết quả
print("Danh sách đã nhập:", DanhSach)
print("Tổng các giá trị chia hết cho 5 là:", Tong)
