#Q2.74
# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử n = "))

# Khởi tạo danh sách rỗng
DanhSach = []

# Nhập các phần tử và lưu vào danh sách
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i + 1}: "))
    DanhSach.append(x)

# Trường hợp danh sách rỗng
if n == 0:
    SoLuongLonNhat = 0
else:
    # Độ dài dãy đan dấu hiện tại
    DoDaiHienTai = 1

    # Độ dài dãy đan dấu lớn nhất
    SoLuongLonNhat = 1

    # Duyệt từ phần tử thứ 2 trở đi
    for i in range(1, n):

        # Nếu tích hai phần tử liên tiếp âm
        # => hai số trái dấu => tiếp tục dãy đan dấu
        if DanhSach[i] * DanhSach[i - 1] < 0:
            DoDaiHienTai += 1

        else:
            # Không đan dấu, bắt đầu dãy mới
            DoDaiHienTai = 1

        # Cập nhật độ dài lớn nhất nếu cần
        if DoDaiHienTai > SoLuongLonNhat:
            SoLuongLonNhat = DoDaiHienTai

# Hiển thị kết quả
print("Danh sách:", DanhSach)
print("Số lượng phần tử của dãy đan dấu liên tiếp dài nhất là:",
      SoLuongLonNhat)



