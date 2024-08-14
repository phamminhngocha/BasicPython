#Q2.11 

# Nhập số nguyên n (n >= 1)
n = int(input("Nhập số nguyên n (n >= 1): "))
if n < 1:
    print(f"n phải nhập giá trị >=1. Chương trình dừng thực hiện!")        
else:
    # Tạo danh sách Ds từ 1 đến n
    Ds = list(range(1, n+1))
    Tong=sum(Ds)
    # in kết quả ra màn hình
    print(f"Tổng các phần tử trong Ds là: {Tong}")
