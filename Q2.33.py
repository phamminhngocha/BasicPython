#Q2.33

n = int(input("Nhập số nguyên dương n: "))  # Nhập số nguyên n từ bàn phím
A = 0
# Tính tổng A theo công thức
for i in range(0, n+1):  # Lặp từ 1 đến n
    A += 4*i + 1
# In kết quả
print("Tổng A =", A)
