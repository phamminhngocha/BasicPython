#Q2.18

# Nhập hai số nguyên từ người dùng
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Kiểm tra xem có ít nhất một số chia hết cho 2 hay không
if a % 2 == 0 or b % 2 == 0:
  # Nếu a chia hết cho 2 hoặc b chia hết cho 2 thì có ít nhất một số chẵn
  print("Trong 2 số a, b có ít nhất một số chẵn")
else:
  # Nếu cả a và b đều không chia hết cho 2 thì cả hai đều là số lẻ
  print("2 số a, b đều là số lẻ")
