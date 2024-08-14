#Q5.18
import numpy as np

def LaMaTranDonVi(MaTran):
  # Kiểm tra kích thước ma trận
  SoHang = MaTran.shape[0]
  SoCot = MaTran.shape[1]
  if SoHang != SoCot:
    return False

  # Tạo ma trận đơn vị
  MaTranDonVi = np.eye(SoHang)

  # So sánh từng phần tử
  return np.array_equal(MaTran, MaTranDonVi)

# Nhập ma trận
print("Nhập ma trận (Các giá trị trong mỗi dòng cách nhau bởi dấu cách. Bấm Enter để nhập dòng tiếp theo.):")
MaTranNhap = []
while True:
  Dong = input()
  if not Dong:
    break
  MaTranNhap.append(list(map(float, Dong.split())))

# Chuyển đổi thành ma trận NumPy
MaTranNumPy = np.array(MaTranNhap)

# Kiểm tra và in kết quả
if LaMaTranDonVi(MaTranNumPy):
  print("Ma trận là ma trận đơn vị.")
else:
  print("Ma trận không phải là ma trận đơn vị.")
