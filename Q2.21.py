#Q2.21
# Nhập số nguyên từ người dùng
a = int(input("Nhập vào một số nguyên: "))

# Tính căn bậc hai của a và làm tròn xuống thành số nguyên
CanBacHai = int(a**0.5)
# Kiểm tra xem bình phương của căn bậc hai có bằng a không
if CanBacHai**2 == a:
    # Nếu bằng thì a là số chính phương
    print(a, "là số chính phương")
else:
    # Nếu không bằng thì a không phải số chính phương
    print(a, "không là số chính phương")
