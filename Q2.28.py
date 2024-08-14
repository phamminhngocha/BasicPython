#Q2.28

# Nhập tháng và năm
Thang = int(input("Nhập tháng (1-12): "))
Nam = int(input("Nhập năm: "))

# Kiểm tra tính hợp lệ của tháng
if Thang < 1 or Thang > 12:
    print("Tháng không hợp lệ.")
else:
    # Xác định số ngày trong tháng
    SoNgay = 31  # Giả định tháng có 31 ngày
    if Thang in [4, 6, 9, 11]:
        SoNgay = 30  # Các tháng 4, 6, 9, 11 có 30 ngày
    elif Thang == 2:
        # Kiểm tra năm nhuận
        if Nam % 4 == 0 and (Nam % 100 != 0 or Nam % 400 == 0):
            SoNgay = 29  # Năm nhuận, tháng 2 có 29 ngày
        else:
            SoNgay = 28  # Năm không nhuận, tháng 2 có 28 ngày

    print(f"Tháng {Thang} năm {Nam} có {SoNgay} ngày.")
