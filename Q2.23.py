#Q2.23
# Nhập vào ba số thực a, b, c
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện để a, b, c là ba cạnh của một tam giác
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    # Kiểm tra loại tam giác
    if a == b == c:
        print("a, b, c là 3 cạnh của một tam giác đều")
    elif a == b or b == c or a == c:
        print("a, b, c là 3 cạnh của một tam giác cân")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("a, b, c là 3 cạnh của một tam giác vuông")
    else:
        print("a, b, c là 3 cạnh của một tam giác thường")
else:
    print("a, b, c không phải là 3 cạnh của một tam giác")
