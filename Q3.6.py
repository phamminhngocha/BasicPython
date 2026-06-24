#Q3.6
# Lưu nội dung code ra file ThoiGian.py
# Import lớp datetime để làm việc với ngày và thời gian
from datetime import datetime
# Hàm lấy ngày hiện tại
def LayNgayHienTai():
    return datetime.now().date()
# Hàm lấy thời gian hiện tại
def LayThoiGianHienTai():
    return datetime.now().time()
# Hàm định dạng ngày giờ theo chuỗi
def DinhDangNgayGio():
    # strftime() dùng để định dạng ngày giờ theo mẫu
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# Lưu nội dung code ra file Main.py
# Import module đã tạo
import ThoiGian
# Gọi hàm lấy ngày hiện tại
NgayHienTai = ThoiGian.LayNgayHienTai()
# Gọi hàm lấy thời gian hiện tại
ThoiGianHienTai = ThoiGian.LayThoiGianHienTai()
# Gọi hàm định dạng ngày giờ
NgayGioDinhDang = ThoiGian.DinhDangNgayGio()
# Hiển thị kết quả
print("Ngày hiện tại:", NgayHienTai)
print("Thời gian hiện tại:", ThoiGianHienTai)
print("Ngày giờ định dạng:", NgayGioDinhDang)
# Gợi ý một số hàm/phương thức khác của module datetime:
# datetime.now()
#   Lấy ngày và giờ hiện tại dưới dạng đối tượng datetime.

# date.today()
#   Lấy ngày hiện tại trực tiếp, ngắn gọn hơn trong trường hợp chỉ cần ngày.

# datetime.strftime()
#   Định dạng ngày giờ thành chuỗi theo nhiều mẫu khác nhau.

# datetime.strptime()
#   Chuyển chuỗi thành đối tượng ngày giờ.

# timedelta()
#   Cộng hoặc trừ số ngày, giờ, phút, giây.

# Điểm tốt của cách xây dựng module:
# - Tái sử dụng được các hàm ở nhiều chương trình khác nhau.
# - Mã nguồn dễ bảo trì và mở rộng.
# - Phân tách rõ phần xử lý và phần giao diện chương trình.
# - Phù hợp với lập trình hướng module trong Python.
