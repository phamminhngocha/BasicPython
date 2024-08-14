#Q2.56

# Nhập số lượng phần tử cần nhập
n = int(input("Nhập số lượng phần tử: "))
# Khởi tạo một danh sách rỗng để lưu trữ các phần tử
DanhSach = []
# Nhập từng phần tử và thêm vào danh sách
for i in range(n):
    # Nhập phần tử bất kỳ thứ i
    PhanTu = input(f"Nhập phần tử thứ {i+1}: ")
    # Thêm phần tử vào danh sách
    DanhSach.append(PhanTu)
# In danh sách vừa nhập
print("Danh sách các phần tử vừa nhập:", DanhSach)
