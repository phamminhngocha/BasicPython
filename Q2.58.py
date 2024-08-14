#Q2.58

# Nhập số lượng phần tử cần nhập
n = int(input("Nhập số lượng phần tử n: "))
# Khởi tạo một list rỗng để lưu trữ các phần tử nhập vào
ListTemp = []
# Nhập từng phần tử và thêm vào list
for i in range(n):
    # Nhập phần tử thứ i và chuyển về kiểu số nguyên
    PhanTu = input(f"Nhập phần tử bất kỳ thứ {i+1}: ")
    # Thêm phần tử vào list
    ListTemp.append(PhanTu)
# Chuyển đổi list thành tuple
Tp = tuple(ListTemp)
# In ra tuple vừa tạo
print("Tuple sau khi nhập:", Tp)
