#Q5.9
import random  # Thư viện để tạo số ngẫu nhiên

def TimSoChanNhoNhat(Mang):  
  SoChanNhoNhat = None  # Khởi tạo giá trị ban đầu cho số chẵn nhỏ nhất
  for So1 in Mang:
    if So1 % 2 == 0:  # Kiểm tra xem số có phải là số chẵn không
      if SoChanNhoNhat is None or So1 < SoChanNhoNhat:
        SoChanNhoNhat = So1  # Cập nhật giá trị số chẵn nhỏ nhất nếu tìm thấy số nhỏ hơn
  return SoChanNhoNhat

# Nhập số lượng phần tử của mảng
SoLuongPhanTu = int(input("Nhập số lượng phần tử của mảng: "))

# Tạo mảng ngẫu nhiên
MangSo = []
for _ in range(SoLuongPhanTu):
  So2 = random.randint(1, 1000)  # Tạo số ngẫu nhiên từ 1 đến 100
  MangSo.append(So2)

# In mảng ra màn hình
print("Mảng vừa tạo:", MangSo)

# Tìm và in ra số chẵn nhỏ nhất
KetQua = TimSoChanNhoNhat(MangSo)
if KetQua is None:
  print("Không tìm thấy số chẵn trong mảng.")
else:
  print("Số chẵn nhỏ nhất trong mảng là:", KetQua)
