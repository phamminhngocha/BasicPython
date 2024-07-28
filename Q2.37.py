#Q2.37
# Nhập giá trị n từ người dùng
n = int(input("Nhập vào số nguyên n (n >= 1): "))  
C = 0
# i lặp từ 1 đến n
for i in range(1, n+1):  
    C += 1/i
# In kết quả
print("Tổng C = ", C)  
