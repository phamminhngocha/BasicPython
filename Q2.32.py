#Q2.32
# Nhập số nguyên n
n = int(input("Nhập vào số nguyên n (n>=1): "))
S = 0
# Tính tổng từ 1 đến n
for i in range(1, n+1):
    S += i
# In ra kết quả
print("Tổng S = ", S)
