#Q2.16
# Nhập số nguyên từ người dùng
a = int(input("Nhập vào một số nguyên: "))
# Kiểm tra xem số a có chia hết cho 3 và nằm trong khoảng 10 đến 50 không
if a % 3 == 0 and 10 <= a <= 50:
    # Nếu cả hai điều kiện đều đúng, in ra "Đúng"
    print("Đúng")
else:
    # Nếu một trong hai điều kiện hoặc cả hai điều kiện đều sai, in ra "Sai"
    print("Sai")
