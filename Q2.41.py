#Q2.41

# Nhập giá trị k từ người dùng
k = float(input("Nhập giá trị k: "))
n = 1
E = 0
# Vòng lặp tính tổng E cho đến khi E lớn hơn hoặc bằng k
while E < k:
    E += (n - 1) / n
    n += 1
# In ra giá trị lớn nhất của n và giá trị tương ứng của E
print("Giá trị lớn nhất của n là:", n - 1)
print("Giá trị lớn nhất của E (nhỏ hơn k) là:", E - (n - 1) / n)
