#T7.2.1: Tối ưu chương trình tìm số nguyên tố
# Hàm kiểm tra có là số nguyên tố không
def LaSoNguyenTo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True   
# Nhập số cần kiểm tra
So = int(input("Nhập một số nguyên dương: "))
# Gọi hàm kiểm tra và in kết quả
if LaSoNguyenTo(So):
    print(So, "là số nguyên tố")
else:
    print(So, "không là số nguyên tố")
