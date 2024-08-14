#Q2.63

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))
# Khởi tạo một danh sách rỗng để lưu trữ các phần tử
DanhSach = []
# Nhập từng phần tử và thêm vào danh sách
for i in range(n):
    # Nhập phần tử thứ i
    x = float(input(f"Nhập phần tử số bất kỳ thứ {i+1}: "))
    # Thêm phần tử x vào danh sách
    DanhSach.append(x)
# Tính tổng các phần tử có giá trị là số nguyên dương.
Tong=0
for j in DanhSach:
    if j>0 and int(j)==j:
        Tong+=j
# In kết quả
print("Tổng các phần tử có giá trị là số nguyên dương là:", Tong)
