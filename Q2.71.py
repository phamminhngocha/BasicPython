#Q2.71
# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử n = "))

# Khởi tạo danh sách rỗng
DanhSach = []

# Nhập các phần tử vào danh sách
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i + 1}: "))
    DanhSach.append(x)  # Thêm phần tử x vào cuối danh sách

# In danh sách ban đầu
print("Danh sách ban đầu:", DanhSach)

# Nhập vị trí phần tử cần xóa
k = int(input("Nhập vị trí k cần xóa (tính từ 1): "))

# Kiểm tra vị trí k có hợp lệ hay không
if 1 <= k <= len(DanhSach):
    del DanhSach[k - 1]  # Xóa phần tử ở vị trí k (do chỉ số list bắt đầu từ 0)

    # In danh sách sau khi xóa
    print("Danh sách sau khi xóa phần tử thứ", k, ":", DanhSach)
else:
    print("Vị trí k không hợp lệ!")
