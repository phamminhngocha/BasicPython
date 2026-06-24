#Q2.73
# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử n = "))

# Khởi tạo danh sách rỗng
DanhSach = []

# Nhập n phần tử và lưu vào danh sách
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i + 1}: "))
    DanhSach.append(x)  # Thêm phần tử x vào cuối danh sách

# Sắp xếp danh sách theo thứ tự giảm dần
DanhSach.sort(reverse=True)

# In danh sách sau khi sắp xếp
print("Danh sách theo thứ tự giảm dần:")
for x in DanhSach:
    print(x, end=" ")

# Ngoài ra, ta có thể sử dụng phương thức sort() hoặc hàm sorted() đáp ứng yêu cầu bài này mà code ngắn gọn, tối ưu hơn

