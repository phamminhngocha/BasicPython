#Q2.42
# Nhập số nguyên dương a từ bàn phím
a = int(input("Nhập vào số nguyên dương a: "))  
print("Các ước của", a, "là:")
# i lặp từ 1 đến a
for i in range(1, a+1):
    # Nếu a chia hết cho i thì i là ước của a
    if a % i == 0:       
        print(i)
