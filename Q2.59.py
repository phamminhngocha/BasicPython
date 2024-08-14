#Q2.59

# Nhập số lượng cặp giá trị muốn tạo
n = int(input("Nhập số lượng cặp giá trị (n): "))
TuDien = {}
# Nhập các cặp khóa-giá trị và thêm vào từ điển
for i in range(n):
    # Nhập khóa
    Key = input(f"Nhập khóa thứ {i+1}: ")
    # Nhập giá trị tương ứng
    Value = input(f"Nhập giá trị cho khóa '{Key}': ")
    # Thêm cặp khóa-giá trị vào từ điển
    TuDien[Key] = Value
# In ra từ điển đã tạo
print("Từ điển đã tạo:", TuDien)
