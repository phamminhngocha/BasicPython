#Q2.34

# Nhập giá trị n từ người dùng
n = int(input("Nhập số nguyên n (n >= 1): "))
F = 0
Dau = 1
# Vòng lặp tính tổng từ 1 đến n
for i in range(1, n+1):
    # Cộng số hạng vào F, đổi dấu ở mỗi lần lặp
    F += Dau * i
    # Đổi dấu cho lần lặp tiếp theo
    Dau = -Dau
# In kết quả
print("Giá trị của F là:", F)
