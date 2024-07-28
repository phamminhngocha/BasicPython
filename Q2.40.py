#Q2.40
# Nhập số nguyên n
n = int(input("Nhập số nguyên n (n>=1): "))
E = 0
# Tính tổng từ 1/2 đến (n-1)/n
for i in range(2, n+1):
    E += (i-1)/i
# In kết quả
print("Tổng E =",E)
