#Q2.77
# Khởi tạo các biến đếm
SoLuongSoNguyen = 0
SoLuongSoThuc = 0
SoLuongChuoi = 0

print("Nhập các giá trị (nhập 0 để kết thúc):")

while True:
    # Nhập dữ liệu dưới dạng chuỗi
    DuLieu = input("Nhập giá trị: ")

    # Điều kiện dừng chương trình
    if DuLieu == "0":
        break

    try:
        # Thử chuyển dữ liệu sang kiểu số nguyên
        int(DuLieu)

        # Nếu thành công thì tăng bộ đếm số nguyên
        SoLuongSoNguyen += 1

    except ValueError:
        try:
            # Nếu không phải số nguyên, thử chuyển sang số thực
            float(DuLieu)

            # Nếu thành công thì tăng bộ đếm số thực
            SoLuongSoThuc += 1

        except ValueError:
            # Nếu không phải số nguyên và cũng không phải số thực
            # thì được xem là chuỗi ký tự
            SoLuongChuoi += 1

# Hiển thị kết quả
print("\nKẾT QUẢ THỐNG KÊ")
print("Số giá trị số nguyên:", SoLuongSoNguyen)
print("Số giá trị số thực :", SoLuongSoThuc)
print("Số giá trị chuỗi   :", SoLuongChuoi)


