#Q2.46

# Nhập hai số nguyên dương a và b
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
Bcnn = max(a, b)
# Vòng lặp tìm BCNN
while True:
    if Bcnn % a == 0 and Bcnn % b == 0:
        break  # Thoát vòng lặp khi tìm thấy BCNN
    Bcnn += 1
# In kết quả
print(f"Bội chung nhỏ nhất của {a} và {b} là:", Bcnn)
