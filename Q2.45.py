#Q2.45
# Nhập hai số nguyên dương từ bàn phím
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
a1=a
b1=b
# Tìm ước chung lớn nhất (UCLN) bằng thuật toán Euclid
while b != 0:
    a, b = b, a % b
# Tìm và in ra các ước chung
Ucln = a
print(f"Ước chung lớn nhất của {a1} và {b1} là: {Ucln}")
