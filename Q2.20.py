#Q2.20

# Nhập số thực a từ người dùng
a = float(input("Nhập vào một số thực a: "))

# Kiểm tra xem phần thập phân của a có bằng 0 không
if a == int(a):
    # Nếu phần thập phân bằng 0 thì a là số nguyên
    if a > 0:
        print("a là số nguyên dương")
    else:
        print("a là số nguyên âm")
else:
    print("a không là số nguyên")
