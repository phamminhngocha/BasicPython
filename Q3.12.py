# Q3.12
'''
Cấu trúc thư mục:
DuAnLogging/
│
├── main.py
│
└── mypackage/
    ├── __init__.py
    ├── module_a.py
    └── module_b.py
'''


# Sao lưu code sau ra file mypackage/module_a.py
import logging
# Tạo logger cho module_a
logger = logging.getLogger(__name__)
def ham_a():
    # Ghi log mức INFO
    logger.info("Đang thực hiện hàm ham_a() trong module_a")
    print("Thực hiện ham_a()")
  
# Sao lưu code sau ra file mypackage/module_b.py
import logging
# Tạo logger cho module_b
logger = logging.getLogger(__name__)
def ham_b():
    # Ghi log mức WARNING
    logger.warning("Đang thực hiện hàm ham_b() trong module_b")
    print("Thực hiện ham_b()")
  
# Sao lưu code sau ra file main.py
import logging
from mypackage.module_a import ham_a
from mypackage.module_b import ham_b
# Thiết lập hệ thống logging
logging.basicConfig(
    filename="app.log",                 # Tên file log
    level=logging.INFO,                 # Mức log tối thiểu được ghi
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
# Ghi log từ chương trình chính
logging.info("Chương trình bắt đầu")
# Gọi các hàm trong các module khác nhau
ham_a()
ham_b()
# Ghi log khi kết thúc chương trình
logging.info("Chương trình kết thúc")


# Một số hàm/phương thức có thể sử dụng tốt hơn
# logging.debug()
# Ghi log chi tiết phục vụ gỡ lỗi.

# logging.error()
# Ghi log khi xảy ra lỗi.

# logging.critical()
# Ghi log lỗi nghiêm trọng.

# logger.exception()
# Tự động ghi thông tin Exception khi bắt lỗi.

# logging.FileHandler()
# Linh hoạt hơn basicConfig(), cho phép quản lý nhiều file log.

# logging.StreamHandler()
# Ghi log ra màn hình console.

# logging.handlers.RotatingFileHandler()
# Tự động tạo file log mới khi file hiện tại quá lớn.

# Điểm tốt:
# - Chương trình trên sử dụng kiến thức Python cơ bản.
# - Mỗi module có logger riêng nên dễ xác định nguồn phát sinh log.
# - Chỉ cấu hình logging một lần trong chương trình chính.
# - Dễ mở rộng khi package có thêm nhiều module khác.


