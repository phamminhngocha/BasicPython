#Q2.76
# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử n = "))

# Khởi tạo danh sách rỗng
DanhSach = []

# Nhập các phần tử của danh sách
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i + 1}: "))
    DanhSach.append(x)  # Thêm phần tử vào cuối danh sách

# --------------------------------------------------
# Tìm đoạn danh sách con chứa các số dương liên tiếp dài nhất
# --------------------------------------------------

# Vị trí bắt đầu của đoạn dương dài nhất
BatDauMax = -1

# Độ dài lớn nhất tìm được
DoDaiMax = 0

# Vị trí bắt đầu của đoạn dương hiện tại
BatDauHienTai = -1

# Độ dài đoạn dương hiện tại
DoDaiHienTai = 0

# Duyệt từng phần tử trong danh sách
for i in range(len(DanhSach)):

    # Nếu phần tử hiện tại là số dương
    if DanhSach[i] > 0:

        # Nếu đây là phần tử dương đầu tiên của đoạn hiện tại
        if DoDaiHienTai == 0:
            BatDauHienTai = i

        # Tăng độ dài đoạn dương hiện tại
        DoDaiHienTai += 1

        # Nếu đoạn hiện tại dài hơn đoạn dài nhất đã biết
        if DoDaiHienTai > DoDaiMax:
            DoDaiMax = DoDaiHienTai
            BatDauMax = BatDauHienTai

    else:
        # Gặp số không dương => kết thúc đoạn dương hiện tại
        DoDaiHienTai = 0

# Lấy đoạn danh sách con dài nhất
if DoDaiMax > 0:
    DanhSachCon = DanhSach[BatDauMax : BatDauMax + DoDaiMax]

    print("Danh sách đã nhập:")
    print(DanhSach)

    print("\nĐoạn danh sách con chứa các số dương liên tiếp nhiều nhất:")
    print(DanhSachCon)

    print("Số phần tử:", DoDaiMax)

else:
    print("Danh sách không có phần tử dương.")
