#Q2.38

# Nhập giá trị n từ bàn phím
n = int(input("Nhập số nguyên n (n>=1): "))  
C = 0
# i lặp từ 1 đến n
for i in range(1, n+1):  
    C += 1 / (2*i - 1)
# In ra kết quả
print("Tổng C =", C)  
