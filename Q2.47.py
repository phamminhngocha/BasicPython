#Q2.47

# Nhập số nguyên dương a
a = int(input("Nhập vào một số nguyên dương: "))
TongUoc = 1
# Tìm các ước của a từ 2 đến a//2
for i in range(2, a//2 + 1):
    if a % i == 0:
        TongUoc += i
# Kiểm tra xem a có phải là số hoàn hảo không
if TongUoc == a:
    print(a, "là số hoàn hảo.")
else:
    print(a, "không phải là số hoàn hảo.")
