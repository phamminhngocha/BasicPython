#Q5.2
# Tạo một mảng hai chiều bằng cách sử dụng list lồng nhau
MangHaiChieu = [[1, 2, 3,4], [4, 5, 6,7], [7, 8, 9,10]]

# In ra kích thước của mảng
SoHang = len(MangHaiChieu)
SoCot = len(MangHaiChieu[0])  # Giả sử tất cả các hàng có cùng số cột
print("Mảng có", SoHang, "hàng và", SoCot, "cột")

# Duyệt qua từng phần tử trong mảng và in ra
for i in range(SoHang):
    for j in range(SoCot):
        print(MangHaiChieu[i][j], end=" ")  # In ra phần tử và thêm một khoảng trắng
    print()  # Xuống dòng sau khi in xong một hàng







