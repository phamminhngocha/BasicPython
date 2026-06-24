#Q3.3
#Lưu thông tin code ra file ThongTinPhanMem.py
# Khai báo các hằng số của chương trình
Version = "1.0"
LastModifyDate = "24/06/2026"

#Lưu thông tin code ra file ChuongTrinhChinh.py
# Import module chứa các hằng số
import ThongTinPhanMem
# Hiển thị thông tin từ module
print("Version:", ThongTinPhanMem.Version)
print("Last Modify Date:", ThongTinPhanMem.LastModifyDate)
print("Author:", ThongTinPhanMem.Author)
print("Company Name:", ThongTinPhanMem.CompanyName)
# Các kiến thức sử dụng:
# import
#     Dùng để nạp một module vào chương trình.

# TênModule.TênBiến
#     Truy cập biến hoặc hằng số được khai báo trong module.

# Gợi ý một số cách khác:
# from ThongTinPhanMem import Version
#     Chỉ import các hằng số cần sử dụng.

# from ThongTinPhanMem import *
#     Truy cập trực tiếp các hằng số mà không cần viết tên module.
#     Tuy nhiên không nên dùng trong chương trình lớn vì dễ trùng tên biến.

# Có thể xây dựng hàm:
# def HienThiThongTin():
#     ...
# để gom các lệnh hiển thị vào một nơi.
# Cách này giúp chương trình dễ bảo trì và tái sử dụng hơn khi số lượng thông tin tăng lên.



