#Q5.6
# Tạo một danh sách rỗng để lưu trữ các giá trị lập phương
LapPhuongCuaSo = []

# Vòng lặp để tính và thêm các giá trị lập phương vào danh sách
for So in range(1, 11):
    # Tính lập phương của số
    LapPhuong = So ** 3
    # Thêm giá trị lập phương vào danh sách
    LapPhuongCuaSo.append(LapPhuong)

# In danh sách các giá trị lập phương
print("Danh sách các giá trị lập phương:", LapPhuongCuaSo)
