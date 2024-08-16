#Q2.66
# Nhập số lượng phần tử 
SoLuongPhanTu = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các phần tử vào danh sách
DanhSach = []
for i in range(SoLuongPhanTu):
  So = float(input(f"Nhập phần tử thứ {i+1}: "))
  DanhSach.append(So)

# Nhập giá trị k 
k = int(input("Nhập giá trị k (1 <= k <= số lượng phần tử): "))

# Khử các giá trị trùng nhau trong DanhSach
DanhSach=list(set(DanhSach))

# Sắp xếp danh sách giảm dần
DanhSach.sort(reverse=True)

# In ra giá trị lớn thứ k
print(DanhSach)
print(f"Giá trị lớn thứ {k} trong danh sách là: {DanhSach[k-1]}")
