#Q2.39
# Nhập giá trị k từ người dùng
k = float(input("Nhập giá trị k: "))
n = 1
D = 0
# Vòng lặp để tính tổng và tăng n cho đến khi D lớn hơn hoặc bằng k
while D <= k:
    D += 1 / (2*n - 1)
    n += 1
# In ra kết quả
print("Giá trị n nhỏ nhất để D(n) > k là:", n-1)
