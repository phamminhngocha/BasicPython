#Q2.70
# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử n = "))

# Khởi tạo danh sách rỗng
DanhSach = []

# Nhập các phần tử của danh sách
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i + 1}: "))
    DanhSach.append(x)  # Thêm phần tử vào cuối danh sách

# Nhập số lần xuất hiện cần tìm
k = int(input("Nhập k = "))

# Từ điển dùng để đếm số lần xuất hiện
Dem = {}

# Duyệt từng phần tử trong danh sách
for x in DanhSach:
    if x in Dem:
        Dem[x] += 1      # Nếu đã có thì tăng bộ đếm lên 1
    else:
        Dem[x] = 1       # Nếu chưa có thì khởi tạo bằng 1

# Tìm các giá trị xuất hiện đúng k lần
KetQua = []

for x in Dem:
    if Dem[x] == k:
        KetQua.append(x)

# Hiển thị kết quả
print("Danh sách đã nhập:", DanhSach)

if len(KetQua) > 0:
    print(f"Các giá trị xuất hiện {k} lần là:", KetQua)
else:
    print(f"Không có giá trị nào xuất hiện {k} lần.")

