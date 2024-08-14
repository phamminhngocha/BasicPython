#Q2.62

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))
# Khởi tạo một tuple rỗng để lưu trữ các phần tử
Tp = ()
# Nhập từng phần tử và thêm vào tuple
for i in range(n):
    # Nhập phần tử thứ i
    x = float(input(f"Nhập phần tử số bất kỳ thứ {i+1}: "))
    # Thêm phần tử x vào tuple
    Tp += (x,)
# Tìm giá trị nhỏ nhất và các chỉ số tương ứng
MinValue = min(Tp)
MinIndices = [i for i, x in enumerate(Tp) if x == MinValue]
# In kết quả
print("Tuple:", Tp)
print("Giá trị nhỏ nhất:", MinValue)
print("Các chỉ số của giá trị nhỏ nhất:", MinIndices)
