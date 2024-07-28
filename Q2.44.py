#Q2.44
# Nhập hai số nguyên dương a và b
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

# Tìm ước chung lớn nhất (UCLN) để tối ưu hóa việc tìm ước chung
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Tìm và in các ước chung
uc = ucln(a, b)
print("Các ước chung của", a, "và", b, "là:")
for i in range(1, uc + 1):
    if a % i == 0 and b % i == 0:
        print(i)
