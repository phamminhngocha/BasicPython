#Q2.53

# Nhập số nguyên dương n từ bàn phím
n = int(input("Nhập số nguyên dương n: "))
n1=n
TongChuSo = 0
while n1 > 0:  # Lặp trong khi n lớn hơn 0
    TongChuSo += n1 % 10  # Lấy chữ số hàng đơn vị và cộng vào tổng
    n1 //= 10  # Loại bỏ chữ số hàng đơn vị
# In ra kết quả
print("Tổng các chữ số của", n, "là:", TongChuSo)  
