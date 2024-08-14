#Q5.13
# Nhập kích thước của ma trận từ người dùng
SoDong = int(input("Nhập số dòng của ma trận: "))
SoCot = int(input("Nhập số cột của ma trận: "))

# Khởi tạo một ma trận rỗng để lưu trữ giá trị
MaTran = []

# Nhập giá trị cho từng phần tử trong ma trận
for i in range(SoDong):  # Lặp qua từng dòng
    Dong1 = []  # Tạo một hàng mới
    for j in range(SoCot):  # Lặp qua từng cột trong dòng
        GiaTri = int(input(f"Nhập giá trị cho phần tử ở hàng {i+1}, cột {j+1}: "))
        Dong1.append(GiaTri)  # Thêm giá trị vào hàng
    MaTran.append(Dong1)  # Thêm hàng vào ma trận

# Hiển thị ma trận
print("Ma trận vừa nhập:")
for Dong2 in MaTran:
    print(Dong2)
