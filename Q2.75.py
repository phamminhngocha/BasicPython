#Q2.75
'''"Số lượng các phần tử không tăng nhiều nhất" là độ dài lớn nhất của một dãy con liên tiếp 
mà mỗi phần tử sau nhỏ hơn hoặc bằng phần tử đứng trước nó.'''

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử n = "))

# Khởi tạo danh sách rỗng
DanhSach = []

# Nhập các phần tử vào danh sách
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i + 1}: "))
    DanhSach.append(x)      # Thêm phần tử vào cuối danh sách

# Trường hợp danh sách rỗng
if n == 0:
    SoLuongLonNhat = 0
else:
    # Độ dài đoạn không tăng hiện tại
    DoDaiHienTai = 1

    # Độ dài đoạn không tăng lớn nhất tìm được
    SoLuongLonNhat = 1

    # Duyệt từ phần tử thứ 2 đến hết danh sách
    for i in range(1, n):

        # Nếu phần tử hiện tại <= phần tử trước đó
        # thì dãy không tăng vẫn tiếp tục
        if DanhSach[i] <= DanhSach[i - 1]:
            DoDaiHienTai += 1

            # Cập nhật độ dài lớn nhất nếu cần
            if DoDaiHienTai > SoLuongLonNhat:
                SoLuongLonNhat = DoDaiHienTai

        else:
            # Dãy không tăng bị ngắt
            # Bắt đầu đếm lại từ phần tử hiện tại
            DoDaiHienTai = 1

# Hiển thị kết quả
print("Danh sách:", DanhSach)
print("Số lượng phần tử không tăng liên tiếp nhiều nhất là:", SoLuongLonNhat)



