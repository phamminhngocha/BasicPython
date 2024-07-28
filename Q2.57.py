#Q2.57
# Nhập số lượng phần tử cần nhập
n = int(input("Nhập số lượng phần tử bạn muốn nhập: "))
# Khởi tạo một tập hợp rỗng
TapHop = set()
# Nhập từng phần tử và thêm vào tập hợp
for i in range(n):
    # Nhập phần tử thứ i
    PhanTu = input(f"Nhập phần tử bất kỳ thứ {i+1}: ")
    # Thêm phần tử vào tập hợp
    TapHop.add(PhanTu)
# In ra tập hợp các phần tử đã nhập
print("Tập hợp các phần tử bạn đã nhập là:", TapHop)
