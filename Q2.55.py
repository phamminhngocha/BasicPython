#Q2.55
# Nhập số nguyên dương k
k = int(input("Nhập số nguyên dương k: "))
# Khởi tạo hai số Fibonacci đầu tiên
Fib1 = 0
Fib2 = 1
# Khởi tạo biến để lưu trữ số Fibonacci tiếp theo
NextFib = 0
# Lặp cho đến khi số Fibonacci tiếp theo lớn hơn k
while NextFib <= k:
    # Tính số Fibonacci tiếp theo
    NextFib = Fib1 + Fib2
    # Cập nhật các số Fibonacci trước đó
    Fib1 = Fib2
    Fib2 = NextFib
# In ra số Fibonacci lớn nhất không vượt quá k
print("Số Fibonacci lớn nhất không vượt quá", k, "là:", Fib1)
