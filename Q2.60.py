#Q2.60

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))
# Khởi tạo một danh sách rỗng để lưu trữ các phần tử
DanhSach = []
# Nhập từng phần tử vào danh sách
for i in range(n):
    # Nhập phần tử thứ i và chuyển đổi thành số nguyên
    PhanTu = float(input(f"Nhập giá trị số bất kỳ cho phần tử thứ {i+1}: "))
    # Thêm phần tử vào danh sách
    DanhSach.append(PhanTu)
# Khởi tạo biến để lưu tổng các số nguyên dương
Tong = 0
# Duyệt qua từng phần tử trong danh sách
for So in DanhSach:
    # Nếu số đó lớn hơn 0 và là số nguyên thì tính tổng
    if So > 0 and int(So)==So:
        # Cộng số đó vào tổng
        Tong += So
# In ra kết quả
print("Tổng các số nguyên dương trong danh sách là:", Tong)
