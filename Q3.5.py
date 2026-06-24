#Q3.5
# Lưu code sau ra file XuLyChuoi.py
#  Module XuLyChuoi.py
# Chứa các hàm xử lý chuỗi cơ bản
def DaoNguocChuoi(chuoi):
    # Dùng vòng lặp duyệt từ cuối chuỗi về đầu
    # Tạo chuỗi mới sau khi đảo ngược
    ket_qua = ""
    for i in range(len(chuoi) - 1, -1, -1):
        ket_qua += chuoi[i]
    return ket_qua
def DemKyTu(chuoi):
    # Hàm len() trả về số lượng ký tự trong chuỗi
    return len(chuoi)
def ThayTheKyTu(chuoi, kyTuCu, kyTuMoi):
    # Duyệt từng ký tự trong chuỗi
    # Nếu gặp ký tự cần thay thì thay bằng ký tự mới
    ket_qua = ""
    for kyTu in chuoi:
        if kyTu == kyTuCu:
            ket_qua += kyTuMoi
        else:
            ket_qua += kyTu
    return ket_qua

# Lưu code sau ra file ChuongTrinh.py
# Import module xử lý chuỗi
import XuLyChuoi
# Nhập chuỗi từ người dùng
Chuoi = input("Nhập chuỗi cần xử lý: ")
# Gọi hàm đảo ngược chuỗi trong module
ChuoiDaoNguoc = XuLyChuoi.DaoNguocChuoi(Chuoi)
# Gọi hàm đếm số ký tự
SoKyTu = XuLyChuoi.DemKyTu(Chuoi)
# Nhập ký tự cần thay thế
KyTuCu = input("Nhập ký tự cần thay thế: ")
KyTuMoi = input("Nhập ký tự thay thế: ")
# Gọi hàm thay thế ký tự
ChuoiMoi = XuLyChuoi.ThayTheKyTu(
    Chuoi,
    KyTuCu,
    KyTuMoi
)
# Xuất kết quả
print("\nKẾT QUẢ XỬ LÝ")
print("Chuỗi ban đầu:", Chuoi)
print("Chuỗi đảo ngược:", ChuoiDaoNguoc)
print("Số ký tự trong chuỗi:", SoKyTu)
print("Chuỗi sau thay thế:", ChuoiMoi)

# Gợi ý mở rộng:
# 1. Có thể dùng phương thức:
#    chuoi[::-1]
#    để đảo ngược chuỗi nhanh hơn.
#    Ưu điểm:
#       - Code ngắn gọn.
#       - Tốc độ xử lý tốt vì Python tối ưu thao tác slicing.

# 2. Có thể dùng:
#    chuoi.replace(kyTuCu, kyTuMoi)
#    để thay thế ký tự.
#    Ưu điểm:
#       - Không cần tự viết vòng lặp.
#       - Dễ đọc và ít lỗi hơn.

# 3. Có thể dùng:
#    chuoi.count(kyTu)
#    để đếm số lần xuất hiện của một ký tự.
#    Ưu điểm:
#       - Nhanh hơn so với tự duyệt chuỗi.

# 4. Các phương thức trên thường có độ phức tạp O(n),
#    tương đương thuật toán tự xây dựng,
#    nhưng được Python tối ưu bên trong nên chạy hiệu quả hơn.

