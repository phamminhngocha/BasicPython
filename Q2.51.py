#Q2.51

# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập vào một số nguyên dương n: "))
n1=n
Dem = 0
# Kiểm tra xem n có lớn hơn 0 hay không
if n1 > 0:
    # Vòng lặp while để lặp cho đến khi n bằng 0
    while n1 > 0:
        # Tăng biến đếm lên 1
        Dem += 1
        # Loại bỏ chữ số cuối cùng của n
        n1 //= 10
# In ra kết quả
print("Số lượng chữ số của", n, "là:", Dem)
