#Q2.22

# Nhập vào ba số thực a, b, c từ bàn phím
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện để ba số a, b, c là ba cạnh của một tam giác
# Điều kiện: 3 giá trị phải >0 và tổng của hai cạnh bất kỳ phải lớn hơn cạnh còn lại
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print(f"{a}, {b}, {c} là 3 cạnh của một tam giác")
else:
    print(f"{a}, {b}, {c} không phải là 3 cạnh của một tam giác")
