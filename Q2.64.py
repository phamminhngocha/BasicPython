#Q2.64

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
# Tìm vị trí của phần tử đầu tiên (Tính từ trái qua phải) là số âm
ViTri=-1
for k,j in enumerate(DanhSach):
    if j<0:
        ViTri=k+1
        break
# In kết quả
if ViTri==-1:
    print("Trong danh sách không có số âm:")
else:
    print("vị trí của phần tử đầu tiên (Tính từ trái qua phải) là số âm:", ViTri)
