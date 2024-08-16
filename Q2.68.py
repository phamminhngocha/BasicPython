#Q2.68
# Nhập số lượng phần tử
SoLuongPhanTu = int(input("Nhập số lượng phần tử: "))

# Khởi tạo danh sách rỗng để lưu trữ các phần tử
DanhSach = []

# Nhập các phần tử vào danh sách
for i in range(SoLuongPhanTu):
  So = float(input(f"Nhập phần tử thứ {i+1}: "))
  DanhSach.append(So)

# Tạo một từ điển để đếm số lần xuất hiện của mỗi phần tử
DemSoLanXuatHien = {}
for PhanTu in DanhSach:
    if PhanTu in DemSoLanXuatHien:
        DemSoLanXuatHien[PhanTu] += 1
    else:
        DemSoLanXuatHien[PhanTu] = 1

# Tìm giá trị lớn nhất trong số lần xuất hiện
GiaTriLonNhat = max(DemSoLanXuatHien.values())

# Tìm các phần tử có số lần xuất hiện lớn nhất
CacPhanTuXuatHienNhieuNhat = []
for PhanTu, SoLan in DemSoLanXuatHien.items():
    if SoLan == GiaTriLonNhat:
        CacPhanTuXuatHienNhieuNhat.append(PhanTu)

# In kết quả
print("Các phần tử xuất hiện nhiều nhất là:", CacPhanTuXuatHienNhieuNhat)

