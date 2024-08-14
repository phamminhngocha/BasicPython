#Q2.15

# Nhập số nguyên từ người sử dụng và chuyển đổi thành kiểu số nguyên
a = int(input("Nhập vào một số nguyên: "))

# Kiểm tra xem số a có chia hết cho 2 không
if a % 2 == 0:
    # Nếu a chia hết cho 2 (số dư bằng 0) thì in ra "a là số chẵn"
    print(a, "là số chẵn")
else:
    # Nếu a không chia hết cho 2 (số dư khác 0) thì in ra "a là số lẻ"
    print(a, "là số lẻ")
