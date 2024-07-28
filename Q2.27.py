#Q2.27
import math  # Nhập thư viện math để sử dụng hàm căn bậc hai
# Nhập các hệ số a, b, c từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Tính Delta
Delta = b**2 - 4*a*c

# Kiểm tra các trường hợp của delta
if Delta > 0:
    x1 = (-b + math.sqrt(Delta)) / (2*a)
    x2 = (-b - math.sqrt(Delta)) / (2*a)
    print("Phương trình có hai nghiệm phân biệt: x1 =", x1, "và x2 =", x2)
elif Delta == 0:
    x = -b / (2*a)
    print("Phương trình có nghiệm kép: x =", x)
else:
    print("Phương trình vô nghiệm")
