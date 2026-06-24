#Q3.1
# Lưu code sau ra File: KiemTra.py
def SoTuNhien(x):
    """
    Hàm kiểm tra x có phải số tự nhiên hay không.
    Trả về:
        True  : nếu x là số tự nhiên
        False : nếu không phải số tự nhiên
    """
    # Kiểm tra kiểu dữ liệu là số nguyên
    # và giá trị không âm
    if isinstance(x, int) and x >= 0:
        return True
    else:
        return False


# Lưu code sau ra  File: Main.py
# Nhập hàm SoTuNhien từ module KiemTra
from KiemTra import SoTuNhien
# Nhập dữ liệu từ bàn phím
x = int(input("Nhập một số nguyên: "))
# Gọi hàm trong module để kiểm tra
if SoTuNhien(x):
    print(x, "là số tự nhiên")
else:
    print(x, "không phải số tự nhiên")
