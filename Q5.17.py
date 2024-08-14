#Q5.17
import numpy as np

def TinhTongDuongCheoChinh(MaTran):  
  # Lấy kích thước của ma trận
  SoDong, SoCot = MaTran.shape

  # Khởi tạo biến tổng
  Tong = 0

  # Duyệt qua các phần tử trên đường chéo chính
  for i in range(SoDong):
    Tong += MaTran[i][i]

  return Tong

# Nhập kích thước của ma trận
n = int(input("Nhập kích thước của ma trận vuông: "))

# Khởi tạo ma trận
MaTran = np.zeros((n, n))

# Nhập các phần tử của ma trận
print("Nhập các phần tử của ma trận:")
for i in range(n):
  for j in range(n):
    MaTran[i][j] = float(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))

# Gọi hàm tính tổng và in kết quả
KetQua = TinhTongDuongCheoChinh(MaTran)
print("Tổng các phần tử trên đường chéo chính là:", KetQua)







