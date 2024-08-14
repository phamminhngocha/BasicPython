#Q2.36

# Nhập số nguyên n
n = int(input("Nhập số nguyên n (n >= 1): "))
GiaiThua = 1
# Tính giai thừa bằng vòng lặp for
if n >= 0:
    for i in range(1, n+1):
        GiaiThua *= i
# In kết quả
print(n, "! =", GiaiThua)
