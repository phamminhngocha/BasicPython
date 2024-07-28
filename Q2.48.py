#Q2.48
# Nhập số nguyên dương a từ bàn phím
a = int(input("Nhập vào một số nguyên dương: "))
# Khởi tạo biến flag để kiểm tra tính nguyên tố
Flag = True
# Nếu a nhỏ hơn hoặc bằng 1 thì không phải số nguyên tố
if a <= 1:
    Flag = False
# Duyệt từ 2 đến căn bậc hai của a
for i in range(2, int(a**(1/2)) + 1):
    # Nếu a chia hết cho i thì không phải số nguyên tố
    if a % i == 0:
        Flag = False
        break
# In kết quả
if Flag:
    print(a, "là số nguyên tố")
else:
    print(a, "không phải là số nguyên tố")
