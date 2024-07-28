#Q2.50
# Khởi tạo một list rỗng để lưu trữ các số nguyên
Numbers = []
# Nhập số liên tục cho đến khi người dùng nhập -1
Number = int(input("Nhập số (nhập -1 để kết thúc): "))
while Number != -1:
    Numbers.append(Number)  # Thêm số vào danh sách
    Number = int(input("Nhập số (nhập -1 để kết thúc): "))

# Kiểm tra xem danh sách có phần tử nào không
if len(Numbers) > 0:
    # Tìm số lớn nhất và số nhỏ nhất trong danh sách
    MaxNumber = max(Numbers)
    MinNumber = min(Numbers)
    # In kết quả
    print("Số lớn nhất:", MaxNumber)
    print("Số nhỏ nhất:", MinNumber)
else:
    print("Bạn chưa nhập số nào!")
