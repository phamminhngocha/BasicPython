#Q7.4
# Lưu ý: Các giải thuật sắp xếp trong chương trình này
# gần như không chấp nhận được về mặt thời gian khi sắp xếp dữ liệu lớn do độ phức tạp khá cao


#Thư viện cho phép gửi các yêu cầu HTTP (như GET, POST, PUT, DELETE,...) đến một URL cụ thể và nhận lại phản hồi từ server.
import requests 
# Thư viện cung cấp các hàm để làm việc với thời gian
import time

def DocDuLieuTuFile(TenFile):
  """
  Hàm đọc dữ liệu từ file text và trả về một danh sách các số.
  Args:
    TenFile: Tên file cần đọc.
  Returns:
    Một danh sách chứa các số đọc được từ file.
  """
  print("Đang đọc file dữ liệu số...")
  response = requests.get(TenFile).text[9:] #Lấy từ ký tự có chỉ mục 9 trở đi nhằm bỏ chuỗi ký tư: Numbers
  DanhSachSo = [int(so) for so in response.split()]
  return DanhSachSo

def GhiDuLieuVaoFile(DanhSachSo, TenFile):
  """
  Hàm ghi danh sách các số vào file text.
  Args:
    DanhSachSo: Danh sách các số cần ghi.
    TenFile: Tên file cần ghi.
  """
  with open(TenFile, 'w') as file:
    for so in DanhSachSo:
      file.write(str(so) + '\n')

def SapXepNoiBot(DanhSach):
  """
  Hàm thực hiện sắp xếp nổi bọt cho một danh sách số.
  Args:
    DanhSach: Danh sách các số cần sắp xếp.
  Returns:
    Danh sách đã được sắp xếp.
  """
  n = len(DanhSach)
  # Vòng lặp bên ngoài: Duyệt qua từng phần tử trong danh sách
  for i in range(n):
    # Cờ đánh dấu xem có xảy ra hoán đổi nào trong vòng lặp này không
    DaHoanDoi = False

    # Vòng lặp bên trong: So sánh và hoán đổi các phần tử kề nhau
    for j in range(0, n-i-1):
      # Nếu phần tử bên trái lớn hơn phần tử bên phải thì hoán đổi
      if DanhSach[j] > DanhSach[j+1]:
        DanhSach[j], DanhSach[j+1] = DanhSach[j+1], DanhSach[j]
        DaHoanDoi = True
    # Nếu không có hoán đổi nào xảy ra trong vòng lặp này nghĩa là danh sách đã được sắp xếp
    if not DaHoanDoi:
      break
  return DanhSach

def SapXepChen(DanhSachSo):
  """
  Hàm thực hiện sắp xếp chèn cho một danh sách số.
  Args:
    DanhSachSo: Danh sách các số cần sắp xếp.
  Returns:
    Danh sách đã được sắp xếp.
  """
  SoLuongPhanTu = len(DanhSachSo)
  # Bắt đầu từ phần tử thứ hai (vì phần tử đầu tiên luôn được coi là đã sắp xếp)
  for i in range(1, SoLuongPhanTu):
    # Lưu giá trị của phần tử hiện tại vào một biến tạm thời
    GiaTriHienTai = DanhSachSo[i]
    # Vị trí của phần tử cần chèn
    ViTriChen = i - 1
    # So sánh và dịch chuyển các phần tử lớn hơn giá trị hiện tại về bên phải
    while ViTriChen >= 0 and DanhSachSo[ViTriChen] > GiaTriHienTai:
      DanhSachSo[ViTriChen + 1] = DanhSachSo[ViTriChen]
      ViTriChen -= 1
    # Chèn giá trị hiện tại vào vị trí thích hợp
    DanhSachSo[ViTriChen + 1] = GiaTriHienTai
  return DanhSachSo

def SapXepChon(DanhSachSo):
  """
  Hàm thực hiện sắp xếp một danh sách số theo thuật toán sắp xếp chọn.
  Args:
    DanhSachSo: Danh sách các số cần sắp xếp.
  Returns:
    Danh sách đã được sắp xếp.
  """
  SoLuongPhanTu = len(DanhSachSo)
  # Vòng lặp qua từng phần tử trong danh sách
  for i in range(SoLuongPhanTu):
    # Giả định phần tử đầu tiên của phần chưa sắp xếp là nhỏ nhất
    ViTriPhanTuNhoNhat = i
    # Tìm phần tử nhỏ nhất trong phần chưa sắp xếp
    for j in range(i+1, SoLuongPhanTu):
      if DanhSachSo[j] < DanhSachSo[ViTriPhanTuNhoNhat]:
        ViTriPhanTuNhoNhat = j
    # Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên của phần chưa sắp xếp
    DanhSachSo[i], DanhSachSo[ViTriPhanTuNhoNhat] = DanhSachSo[ViTriPhanTuNhoNhat], DanhSachSo[i]
  return DanhSachSo

def SapXepTron(DanhSachSo):
  """
  Hàm thực hiện sắp xếp trộn cho một danh sách.
  Args:
    DanhSachSo: Danh sách các số cần sắp xếp.
  Returns:
    Danh sách đã được sắp xếp.
  """
  # Kiểm tra độ dài danh sách
  DoDaiDanhSachSo = len(DanhSachSo)
  # Trường hợp danh sách có 1 phần tử hoặc ít hơn thì đã sắp xếp
  if DoDaiDanhSachSo <= 1:
    return DanhSachSo
  # Tìm vị trí chia danh sách thành 2 nửa
  ViTriGiua = DoDaiDanhSachSo // 2
  # Gọi đệ quy để sắp xếp 2 nửa danh sách
  NuaTrai = SapXepTron(DanhSachSo[:ViTriGiua])
  NuaPhai = SapXepTron(DanhSachSo[ViTriGiua:])
  # Trộn hai nửa đã sắp xếp
  return TronHaiNua(NuaTrai, NuaPhai)

def TronHaiNua(NuaTrai, NuaPhai):
  """
  Hàm trộn hai nửa danh sách đã sắp xếp thành một danh sách duy nhất.
  Args:
    NuaTrai: Nửa trái của danh sách.
    NuaPhai: Nửa phải của danh sách.
  Returns:
    Danh sách đã được trộn và sắp xếp.
  """
  # Khởi tạo danh sách kết quả và các chỉ số
  DanhSachSoKetQua = []
  ViTriTrai = 0
  ViTriPhai = 0
  # So sánh và thêm phần tử vào danh sách kết quả
  while ViTriTrai < len(NuaTrai) and ViTriPhai < len(NuaPhai):
    if NuaTrai[ViTriTrai] <= NuaPhai[ViTriPhai]:
      DanhSachSoKetQua.append(NuaTrai[ViTriTrai])
      ViTriTrai += 1
    else:
      DanhSachSoKetQua.append(NuaPhai[ViTriPhai])
      ViTriPhai += 1
  # Thêm các phần tử còn lại (nếu có) vào danh sách kết quả
  while ViTriTrai < len(NuaTrai):
    DanhSachSoKetQua.append(NuaTrai[ViTriTrai])
    ViTriTrai += 1
  while ViTriPhai < len(NuaPhai):
    DanhSachSoKetQua.append(NuaPhai[ViTriPhai])
    ViTriPhai += 1
  return DanhSachSoKetQua

def SapXepNhanh(DanhSachSo):
  """
  Hàm thực hiện sắp xếp nhanh cho một danh sách số.
  Args:
    DanhSachSo: Danh sách các số cần sắp xếp.
  Returns:
    Danh sách đã được sắp xếp.
  """
  # Kiểm tra trường hợp danh sách có ít hơn 2 phần tử thì không cần sắp xếp
  DoDaiDanhSachSo = len(DanhSachSo)
  if DoDaiDanhSachSo <= 1:
    return DanhSachSo
  # Chọn phần tử cuối làm phần tử mốc (pivot)
  PhanTuMoc = DanhSachSo[-1]
  # Tạo hai danh sách con: các phần tử nhỏ hơn pivot và các phần tử lớn hơn hoặc bằng pivot
  DanhSachSoConNhoHon = []
  DanhSachSoConLonHon = []
  for so in DanhSachSo[:-1]:
    if so < PhanTuMoc:
      DanhSachSoConNhoHon.append(so)
    else:
      DanhSachSoConLonHon.append(so)
  # Gọi đệ quy để sắp xếp hai danh sách con
  DanhSachSoConNhoHonSapXep = SapXepNhanh(DanhSachSoConNhoHon)
  DanhSachSoConLonHonSapXep = SapXepNhanh(DanhSachSoConLonHon)
  # Kết hợp danh sách con đã sắp xếp, phần tử mốc và danh sách con lớn hơn đã sắp xếp
  return DanhSachSoConNhoHonSapXep + [PhanTuMoc] + DanhSachSoConLonHonSapXep

# Đọc dữ liệu từ file
TenFileNguon = "https://raw.githubusercontent.com/phamminhngocha/BigData/main/Number%20Values.txt?zarsrc=1303&utm_source=zalo&utm_medium=zalo&utm_campaign=zalo"
DanhSachSo = DocDuLieuTuFile(TenFileNguon)

# Cung cấp thông tin ảnh báo về thời gian sắp xếp
print(f"Danh sách số cần sắp xếp có {len(DanhSachSo)} giá trị!")
print("Mỗi giải thuật sắp xếp sẽ mất thời gian khá dài!!!")
    
# Sắp xếp và ghi kết quả ra các file tương ứng cho mỗi giải thuật:
ThoiGianBatDau = time.time()
ThoiGian1 = time.localtime(ThoiGianBatDau)
Gio1 = time.strftime("%H:%M:%S", ThoiGian1)
print(f"Giải thuật Nổi bọt:\n Thời gian bắt đầu:{Gio1}")
DanhSachSapXep = SapXepNoiBot(DanhSachSo.copy())
GhiDuLieuVaoFile(DanhSachSapXep, "BubbleSort.txt")
ThoiGianKetThuc = time.time()
ThoiGianThucHien = ThoiGianKetThuc- ThoiGianBatDau
ThoiGian2 = time.localtime(ThoiGianKetThuc)
Gio2 = time.strftime("%H:%M:%S", ThoiGian2)
print(f"Thời gian kết thúc:{Gio2}")
print(f"Thời gian thực hiện:{ThoiGianThucHien//3600} giờ {ThoiGianThucHien % 3600 // 60} phút {ThoiGianThucHien // 60} giây \n")

ThoiGianBatDau = time.time()
ThoiGian1 = time.localtime(ThoiGianBatDau)
Gio1 = time.strftime("%H:%M:%S", ThoiGian1)
print(f"Giải thuật Chèn:\n Thời gian bắt đầu:{Gio1}")
DanhSachSapXep = SapXepChen(DanhSachSo.copy())
GhiDuLieuVaoFile(DanhSachSapXep, "InsertionSort.txt")
ThoiGianThucHien = ThoiGianKetThuc- ThoiGianBatDau
ThoiGian2 = time.localtime(ThoiGianKetThuc)
Gio2 = time.strftime("%H:%M:%S", ThoiGian2)
print(f"Thời gian kết thúc:{Gio2}")
print(f"Thời gian thực hiện:{ThoiGianThucHien//3600} giờ {ThoiGianThucHien % 3600 // 60} phút {ThoiGianThucHien // 60} giây \n")

ThoiGianBatDau = time.time()
ThoiGian1 = time.localtime(ThoiGianBatDau)
Gio1 = time.strftime("%H:%M:%S", ThoiGian1)
print(f"Giải thuật Chọn:\n Thời gian bắt đầu:{Gio1}")
DanhSachSapXep = SapXepChon(DanhSachSo.copy())
GhiDuLieuVaoFile(DanhSachSapXep, "SelectionSort.txt")
ThoiGian2 = time.localtime(ThoiGianKetThuc)
Gio2 = time.strftime("%H:%M:%S", ThoiGian2)
print(f"Thời gian kết thúc:{Gio2}")
print(f"Thời gian thực hiện:{ThoiGianThucHien//3600} giờ {ThoiGianThucHien % 3600 // 60} phút {ThoiGianThucHien // 60} giây \n")

ThoiGianBatDau = time.time()
ThoiGian1 = time.localtime(ThoiGianBatDau)
Gio1 = time.strftime("%H:%M:%S", ThoiGian1)
print(f"Giải thuật Trộn:\n Thời gian bắt đầu:{Gio1}")
DanhSachSapXep = SapXepTron(DanhSachSo.copy())
GhiDuLieuVaoFile(DanhSachSapXep, "MergeSort.txt")
ThoiGian2 = time.localtime(ThoiGianKetThuc)
Gio2 = time.strftime("%H:%M:%S", ThoiGian2)
print(f"Thời gian kết thúc:{Gio2}")
print(f"Thời gian thực hiện:{ThoiGianThucHien//3600} giờ {ThoiGianThucHien % 3600 // 60} phút {ThoiGianThucHien // 60} giây \n")

ThoiGianBatDau = time.time()
ThoiGian1 = time.localtime(ThoiGianBatDau)
Gio1 = time.strftime("%H:%M:%S", ThoiGian1)
print(f"Giải thuật Sắp xếp nhanh:\n Thời gian bắt đầu:{Gio1}")
DanhSachSapXep = SapXepNhanh(DanhSachSo.copy())
GhiDuLieuVaoFile(DanhSachSapXep, "QuickSort.txt")
ThoiGian2 = time.localtime(ThoiGianKetThuc)
Gio2 = time.strftime("%H:%M:%S", ThoiGian2)
print(f"Thời gian kết thúc:{Gio2}")
print(f"Thời gian thực hiện:{ThoiGianThucHien//3600} giờ {ThoiGianThucHien % 3600 // 60} phút {ThoiGianThucHien // 60} giây \n")


ThoiGianBatDau = time.time()
ThoiGian1 = time.localtime(ThoiGianBatDau)
Gio1 = time.strftime("%H:%M:%S", ThoiGian1)
print(f"Phương thức sort của list trong python:\n Thời gian bắt đầu:{Gio1}")
DanhSachSapXep=DanhSachSo.copy()
DanhSachSapXep.sort()
GhiDuLieuVaoFile(DanhSachSapXep, "ListSort.txt")
ThoiGianKetThuc = time.time()
ThoiGianThucHien = ThoiGianKetThuc- ThoiGianBatDau
ThoiGian2 = time.localtime(ThoiGianKetThuc)
Gio2 = time.strftime("%H:%M:%S", ThoiGian2)
print(f"Thời gian kết thúc:{Gio2}")
print(f"Thời gian thực hiện:{ThoiGianThucHien//3600} giờ {ThoiGianThucHien % 3600 // 60} phút {ThoiGianThucHien // 60} giây \n")

