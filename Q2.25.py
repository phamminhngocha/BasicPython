#Q2.25
# Nhập điểm trung bình chung học tập từ người dùng
DTBCHT = float(input("Nhập điểm trung bình chung học tập: "))

# Xếp loại học tập dựa trên điểm trung bình
if 0 <= DTBCHT < 4:
    print("Xếp loại: Yếu")
elif 4 <= DTBCHT < 6:
    print("Xếp loại: Trung bình")
elif 6 <= DTBCHT < 7:
    print("Xếp loại: Trung bình-Khá")
elif 7 <= DTBCHT < 8:
    print("Xếp loại: Khá")
elif 8 <= DTBCHT < 9:
    print("Xếp loại: Giỏi")
elif 9 <= DTBCHT <= 10:
    print("Xếp loại: Xuất sắc")
else:
    print("Giá trị điểm trung bình chung học tập nhập không hợp lệ")
