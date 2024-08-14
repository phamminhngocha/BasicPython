#Q2.43

# Nhập số nguyên dương từ người dùng
a = int(input("Nhập vào số nguyên dương a: "))
Dem = 0
# Duyệt qua các số từ 1 đến căn bậc hai của a
for i in range(1, int(a**(1/2)) + 1):
    # Nếu a chia hết cho i thì cả a/i cũng là ước số
    if a % i == 0:
        Dem += 1
        # Nếu i khác a/i thì cộng thêm 1 ước nữa
        if i != a // i:
            Dem += 1
# In ra kết quả
print("Số lượng ước số của", a, "là:", Dem)
