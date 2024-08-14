#Q5.20
import numpy as np

def LaMaTranDoiXung(MaTran):
  # Ma trận chuyển vị
  MaTranChuyenVi = np.transpose(MaTran)

  # So sánh ma trận gốc và ma trận chuyển vị
  return np.array_equal(MaTran, MaTranChuyenVi)

# Nhập ma trận từ người dùng
print("Nhập ma trận (mỗi dòng cách nhau bởi dấu cách):")
MaTranNhap = []
while True:
  Dong = input()
  if not Dong:
    break
  MaTranNhap.append(list(map(float, Dong.split())))

# Chuyển đổi thành ma trận NumPy
MaTranNumpy = np.array(MaTranNhap)

# Kiểm tra và in kết quả
if LaMaTranDoiXung(MaTranNumpy):
  print("Ma trận là ma trận đối xứng.")
else:
  print("Ma trận không phải là ma trận đối xứng.")
