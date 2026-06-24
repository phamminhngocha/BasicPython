#Q3.4
# Lưu code ra file mymodule.py
# Hàm thực hiện phép chia hai số
def chia_hai_so(a, b):
    # Nếu mẫu số bằng 0 thì ném ngoại lệ
    if b == 0:
        raise ZeroDivisionError("Không thể chia cho 0")    
    # Trả về kết quả phép chia
    return a / b

# Lưu code ra file main.py
# Import hàm từ module
from mymodule import chia_hai_so
# Nhập dữ liệu từ bàn phím
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
try:
    # Gọi hàm có thể phát sinh ngoại lệ
    ket_qua = chia_hai_so(a, b)
    # Hiển thị kết quả nếu không có lỗi
    print("Kết quả =", ket_qua)
except ZeroDivisionError as loi:
    # Xử lý ngoại lệ được ném từ module
    print("Lỗi:", loi)

# Gợi ý mở rộng
# raise
# Dùng để chủ động ném một ngoại lệ.

# try ... except
# Dùng để bắt và xử lý ngoại lệ.

# Exception
# Có thể dùng để bắt nhiều loại ngoại lệ khác nhau.
#
# except Exception as loi:

# ValueError
# Thường dùng khi dữ liệu nhập không đúng định dạng.

# FileNotFoundError
# Thường dùng khi thao tác với tệp tin.

# Có thể tự định nghĩa ngoại lệ:

# class LoiDuLieu(Exception):
#     pass

# Ưu điểm:
# - Giúp mô tả lỗi rõ ràng hơn.
# - Dễ bảo trì khi chương trình lớn.
