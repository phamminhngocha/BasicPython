#Q2.61
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
Dem=0
# Duyệt qua từng phần tử trong danh sách
for So in DanhSach:
    # Nếu số đó chia hết cho 5 thì tính tổng
    if So %5==0:
        Tong += So
        Dem+=1
# In ra kết quả
print("Tổng các số nguyên dương trong danh sách là:", Tong/Dem)
