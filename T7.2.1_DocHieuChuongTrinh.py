#T7.2.1: Đọc hiểu chương trình
# Comment 1
def KiemTra (n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    i = 4
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 1
    return True   
# Comment 2
So = int(input("Nhập số: "))
# Comment 3
if KiemTra(So):
    print(So, ": Thông báo 1.")
else:
    print(So, ": Thông báo 2")
