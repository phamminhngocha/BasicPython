#Q5.21
import numpy as np

def NhanHaiMaTran(MaTranA, MaTranB):
  """
  Hàm nhân hai ma trận.

  Args:
    MaTranA: Ma trận thứ nhất.
    MaTranB: Ma trận thứ hai.

  Returns:
    Ma trận kết quả sau khi nhân hai ma trận.
  """

  # Kiểm tra điều kiện để nhân hai ma trận
  SoCotA = MaTranA.shape[1]
  so_hang_B = MaTranB.shape[0]
  if SoCotA != so_hang_B:
    raise ValueError("Số cột của ma trận A phải bằng số hàng của ma trận B")

  # Tạo ma trận kết quả
  SoHangA = MaTranA.shape[0]
  SoCotB = MaTranB.shape[1]
  MaTranKetQua = np.zeros((SoHangA, SoCotB))

  # Thực hiện phép nhân ma trận
  for i in range(SoHangA):
    for j in range(SoCotB):
      for k in range(SoCotA):
        MaTranKetQua[i][j] += MaTranA[i][k] * MaTranB[k][j]

  return MaTranKetQua

# Nhập thông tin hai ma trận từ người dùng
print("Nhập ma trận A:")
MaTranA = []
while True:
  dong = input()
  if not dong:
    break
  MaTranA.append(list(map(float, dong.split())))

print("Nhập ma trận B:")
MaTranB = []
while True:
  Dong = input()
  if not Dong:
    break
  MaTranB.append(list(map(float, Dong.split())))

# Chuyển đổi danh sách thành ma trận NumPy
MaTranA = np.array(MaTranA)
MaTranB = np.array(MaTranB)

# Gọi hàm nhân ma trận và in kết quả
try:
  KetQua = NhanHaiMaTran(MaTranA, MaTranB)
  print("Ma trận kết quả:")
  print(KetQua)
except ValueError as e:
  print(e)
