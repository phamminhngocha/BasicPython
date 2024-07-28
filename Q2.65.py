#Q2.65
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
# Tìm vị trí của phần tử đầu tiên (Tính từ phải qua trái) là số lẻ và chia hết cho 3.
ViTri=-1
for i in range(len(DanhSach)-1,-1,-1):    
    if DanhSach[i] %3==0 and DanhSach[i] %2!=0:
        ViTri=len(DanhSach)-i
        break
# In kết quả
print(DanhSach)
if ViTri==-1:
    print("Trong danh sách không có số âm:")
else:
    print("Vị trí của phần tử đầu tiên (Tính từ phải qua trái) là số lẻ và chia hết cho 3:", ViTri)
