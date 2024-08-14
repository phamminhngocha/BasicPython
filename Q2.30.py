#Q2.30

# Nhập giá trị a và b từ người dùng
a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))

# In các số chẵn chia hết cho 5 trong đoạn [a, b]
print(f"Các số chẵn chia hết cho 5 trong đoạn [{a},{b}]:")
for i in range(a, b+1):
    if i % 2 == 0 and i % 5 == 0:
        print(i)
