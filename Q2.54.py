#Q2.54

# Nhập số nguyên dương n
n = int(input("Nhập vào một số nguyên dương n: "))
LaHaiMu = True
# Kiểm tra xem n có phải là lũy thừa của 2 hay không
# Nếu n và n-1 không có bit nào chung (n & (n-1) == 0)
# thì n là lũy thừa của 2
if n <= 0 or n & (n - 1) != 0:
    LaHaiMu = False
# In kết quả
if LaHaiMu:
    print(n, "là lũy thừa của 2.")
else:
    print(n, "không phải là lũy thừa của 2.")
