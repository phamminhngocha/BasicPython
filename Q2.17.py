#Q2.17
# Nhập số nguyên từ người dùng
a = int(input("Nhập vào một số nguyên: "))

# Kiểm tra xem số có chia hết cho 5 và không chia hết cho 10 hay không
if a % 5 == 0 and a % 10 != 0:
    # Nếu đúng điều kiện trên, in ra kết quả
    print("a có ký tự số cuối cùng là 5")
else:
    # Nếu không đúng điều kiện trên, in ra kết quả còn lại
    print("a không có ký tự số cuối cùng là 5")
