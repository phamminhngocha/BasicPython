#Q2.29

x = int(input("Nhập một số nguyên dương x: "))  # Nhập số x từ bàn phím

# In các số lẻ dương nhỏ hơn x
for i in range(1, x, 2):  # Lặp từ 1 đến x-1 với bước nhảy là 2 (chỉ lấy số lẻ)
    print(i)
