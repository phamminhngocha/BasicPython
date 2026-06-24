#Q2.78
# Code mẫu kiểm tra chặt giá trị khi nhập n giá trị số nguyên, lưu vào một biến có kiểu list
# Nhập số lượng phần tử của danh sách
while True:
    try:
        n = int(input("Nhập số lượng phần tử n = "))
        # Kiểm tra n phải dương
        if n <= 0:
            print("Lỗi: n phải là số nguyên dương!")
            continue
        break
    except ValueError:
        print("Lỗi: Bạn phải nhập một số nguyên!")

# Khởi tạo danh sách rỗng
DanhSach = []
# Nhập n phần tử số nguyên
for i in range(n):
    while True:
        try:
            # Nhập phần tử thứ i+1
            x = int(input(f"Nhập phần tử thứ {i + 1}: "))
            # Nếu chuyển đổi thành công thì thêm vào danh sách
            DanhSach.append(x)
            # Thoát vòng lặp nhập lại
            break
        except ValueError:
            print("Lỗi: Giá trị nhập vào phải là số nguyên!")
            print("Vui lòng nhập lại.")
# Hiển thị kết quả
print("\nDanh sách đã nhập:")
print(DanhSach)
