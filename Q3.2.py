#Q3.2
# Lưu code này ra MyModule.py
# Hàm chuyển một chữ số (0-9) sang chữ
def SoDonViSangChu(So):
    DanhSachChu = [
        "Không", "Một", "Hai", "Ba", "Bốn",
        "Năm", "Sáu", "Bảy", "Tám", "Chín"
    ]
    # Kiểm tra giá trị hợp lệ
    if 0 <= So <= 9:
        return DanhSachChu[So]
    else:
        return "Không hợp lệ"
# Hàm chuyển một số nguyên sang chữ
def SoSangChu(So):
    # Trường hợp số bằng 0
    if So == 0:
        return "Không"
    KetQua = ""
    # Nếu là số âm
    if So < 0:
        KetQua = "Âm "
        So = abs(So)
    # Chuyển số thành chuỗi để duyệt từng chữ số
    ChuoiSo = str(So)
    for KyTu in ChuoiSo:
        # Chuyển ký tự sang số nguyên
        ChuSo = int(KyTu)
        # Gọi hàm đã xây dựng ở trên
        KetQua += SoDonViSangChu(ChuSo) + " "
    return KetQua.strip()


# Lưu code này ra Main.py
# Import thư viện tự tạo
import MyModule
# Nhập số nguyên từ bàn phím
So = int(input("Nhập số nguyên: "))
# Gọi hàm trong module
KetQua = MyModule.SoSangChu(So)
# Hiển thị kết quả
print("Kết quả:", KetQua)
