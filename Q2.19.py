#Q2.19

# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Kiểm tra xem có ít nhất một số lẻ hay không
if a % 2 != 0 or b % 2 != 0:
    print("Trong 2 số a, b có ít nhất một số lẻ")
else:
    print("2 số a, b đều là số chẵn")
