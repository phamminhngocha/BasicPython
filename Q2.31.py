#Q2.31

# Nhập số nguyên dương y
y = int(input("Nhập số nguyên dương y (1<=y<=9): "))
# Kiểm tra điều kiện của y
if 1 <= y <= 9:
    # In bảng cửu chương của y
    for i in range(1, 11):
        print(f"{y} x {i} = {y*i}")
else:
    print("Số y không hợp lệ. Vui lòng nhập số nguyên dương từ 1 đến 9.")
