#T5.2.1: Hiển thị nội dung 1 cột dữ liệu trong BangLuong.csv :
import pandas as pd
# Đọc dữ liệu từ file CSV vào bộ nhớ
df = pd.read_csv("BangLuong.csv")
# Hiển thị tên các cột có trong file BangLuong.csv
TenCot= df.columns
print("Tên các cột có trong file BangLuong.csv:", TenCot)
# Yêu cầu nhập tên cột từ người dùng
CotCanHienThi = input("Nhập tên cột muốn hiển thị nội dung:")
# Kiểm tra xem cột có tồn tại trong DataFrame không
if CotCanHienThi in TenCot:
    # Hiển thị nội dung cột
    print(df[CotCanHienThi])
else:
    print("Cột",CotCanHienThi,"không có trong BangLuong.csv!")
