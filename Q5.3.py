#Q5.3
# Tạo một danh sách rỗng để lưu trữ các số chia hết cho 5
DanhSachSoChiaHetCho5 = []

# Duyệt qua các số từ 1 đến 100
for So in range(1, 101):
    # Kiểm tra xem số đó có chia hết cho 5 không
    if So % 5 == 0:
        # Nếu chia hết cho 5 thì thêm vào danh sách
        DanhSachSoChiaHetCho5.append(So)

# In ra danh sách các số chia hết cho 5
print("Các số chia hết cho 5 trong đoạn [1, 100] là:")
print(DanhSachSoChiaHetCho5)
