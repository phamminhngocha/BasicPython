#Q2.52
# Nhập số nguyên dương n từ bàn phím
n = int(input("Nhập số nguyên dương n: "))  
DemChan = 0  # Đếm số lượng chữ số chẵn, khởi tạo bằng 0
DemLe = 0  # Đếm số lượng chữ số lẻ, khởi tạo bằng 0
# Duyệt từng chữ số của n
while n > 0:
    # Lấy chữ số hàng đơn vị của n
    ChuSo = n % 10
    # Kiểm tra xem chữ số có chẵn hay lẻ
    if ChuSo % 2 == 0:
        DemChan += 1  # Nếu chẵn, tăng biến đếm số chẵn lên 1
    else:
        DemLe += 1  # Nếu lẻ, tăng biến đếm số lẻ lên 1
    # Loại bỏ chữ số hàng đơn vị
    n //= 10
# In kết quả ra màn hình
print("Số lượng chữ số chẵn:", DemChan)
print("Số lượng chữ số lẻ:", DemLe)
