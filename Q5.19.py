#Q5.19
import numpy as np

def TimMaTranChuyenVi(MaTran):
  return np.transpose(MaTran)

# Nhập ma trận từ người dùng
print("Nhập ma trận (mỗi dòng cách nhau bởi dấu cách):")
MaTranNhap = []
while True:
  Dong = input()
  if not Dong:
    break
  MaTranNhap.append(list(map(float, Dong.split())))

# Chuyển đổi danh sách thành ma trận NumPy
MaTranNumpy = np.array(MaTranNhap)

# Tìm ma trận chuyển vị
MaTranChuyenVi = TimMaTranChuyenVi(MaTranNumpy)

# In kết quả
print("Ma trận chuyển vị:")
print(MaTranChuyenVi)
