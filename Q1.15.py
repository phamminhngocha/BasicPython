#Q1.15
# Kiểu dữ liệu tuple trong Python là một kiểu dữ liệu bất biến, có nghĩa là một khi đã tạo ra một tuple, ta không thể thay đổi các phần tử bên trong nó. Còn kiểu list, một kiểu dữ liệu có thể thay đổi được.
# Các thao tác như thêm, xóa, thay đổi phần tử trong tuple đều không thực hiện được
# Kiểu tuple nhằm bảo đảm an toàn cho dữ liệu, cũng như tăng hiệu suất khi truy xuất và so sánh

# Trong trường hợp ta cần thực hiện các thao tác thay đổi giá trị trong tuple thì chuyển về kiểu list, thực hiện thay đổi, sau đó chuyển về kiểu tuple
Ten = ('Mai', 'Ngọc', 'Nga')
print(Ten)
# Chuyển đổi tuple thành list
TenList = list(Ten)
# Thực hiện các thao tác trên list
TenList.insert(0, 'Hạnh')  # Thêm 'Hạnh' vào đầu
print(TenList)
LanIndex=TenList.index('Ngọc')   #Xác định vị chỉ mục của Ngọc
TenList.insert(LanIndex+1, 'Lan')   # Thêm 'Lan' vào giữa 'Ngọc' và 'Nga'
print(TenList)
TenList.append('Hằng')   # Thêm 'Hằng' vào cuối
print(TenList)
TenList.remove('Nga')    # Xóa 'Nga'
print(TenList)
MaiIndex=Ten.index('Mai')
TenList[MaiIndex+1] = 'Cúc'      # Thay thế 'Mai' bằng 'Cúc'
# Chuyển đổi lại thành tuple (nếu cần)
Ten = tuple(TenList)
print(Ten)


