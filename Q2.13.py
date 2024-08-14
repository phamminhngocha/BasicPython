#Q2.13 

# Nhập số nguyên n từ người dùng
n = int(input("Nhập số nguyên n: "))
# Tạo tuple Tp chứa các phần tử 1, 3, 5, 7, ..., 2n+1
Tp = tuple(range(1, 2*n+2, 2))
# Tính giá trị trung bình cộng và in ra màn hình
TrungBinhCong = sum(Tp)/len(Tp)
print(f"Giá trị trung bình cộng của các phần tử trong Tp là: {TrungBinhCong}")
