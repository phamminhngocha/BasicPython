#Q2.26
# Nhập hệ số a và b từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

# Kiểm tra điều kiện a khác 0 (để đảm bảo phương trình có nghiệm duy nhất)
if a != 0:
    # Tính nghiệm của phương trình
    x = -b / a
    # In ra kết quả
    print("Nghiệm của phương trình là:", x)
else:
    # Nếu a = 0, kiểm tra thêm điều kiện b
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
