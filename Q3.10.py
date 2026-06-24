# Q3.10
'''
Cấu trúc thư mục
project/
│
├── main.py
│
└── configurations/
    ├── __init__.py
    ├── reader.py
    └── settings.py
'''

# Copy code sau ra file configurations/settings.py
# Khai báo các biến cấu hình mặc định
TEN_HE_THONG = "Chuong trinh Quan Ly"
PHIEN_BAN = "1.0"
NGON_NGU = "Tieng Viet"


# Copy code sau ra file configurations/reader.py
# Import module chứa cấu hình
from configurations import settings
# Hàm đọc và hiển thị cấu hình
def hien_thi_cau_hinh():
    print("Tên hệ thống:", settings.TEN_HE_THONG)
    print("Phiên bản:", settings.PHIEN_BAN)
    print("Ngôn ngữ:", settings.NGON_NGU)
# Hàm thay đổi cấu hình
def thiet_lap_ngon_ngu(ngon_ngu_moi):
    settings.NGON_NGU = ngon_ngu_moi
 
# Copy code sau ra file configurations/init.py
# Đánh dấu thư mục configurations là package


# Copy code sau ra file main.py
# Import module xử lý cấu hình
from configurations.reader import hien_thi_cau_hinh
from configurations.reader import thiet_lap_ngon_ngu
# Hiển thị cấu hình ban đầu
print("CẤU HÌNH BAN ĐẦU")
hien_thi_cau_hinh()
# Thiết lập lại cấu hình
thiet_lap_ngon_ngu("English")
print("\nCẤU HÌNH SAU KHI THAY ĐỔI")
hien_thi_cau_hinh()

# Các hàm/phương thức có thể sử dụng để có code tốt hơn
# configparser.ConfigParser()
# Đọc và ghi cấu hình từ file .ini.
# Ưu điểm: cấu hình được lưu ngoài chương trình, dễ chỉnh sửa.

# json.load()
# Đọc cấu hình từ file JSON.
# Ưu điểm: lưu được cấu trúc dữ liệu phức tạp.

# json.dump()
# Ghi cấu hình ra file JSON.
# Ưu điểm: lưu lại các thay đổi sau khi chương trình kết thúc.

# pathlib.Path()
# Quản lý đường dẫn file cấu hình an toàn hơn.

# os.getenv()
# Đọc cấu hình từ biến môi trường.
# Ưu điểm: phù hợp cho mật khẩu, khóa API và triển khai thực tế.
