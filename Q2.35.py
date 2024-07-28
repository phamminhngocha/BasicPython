#Q2.35
# Nhập số nguyên n
n = int(input("Nhập số nguyên n (n>=1): "))  
B = 0
#i lặp từ 1 đến n
for i in range(1, n+1): 
    B += i**i
# In kết quả
print("Tổng B =", B)
