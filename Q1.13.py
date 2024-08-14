#Q1.13 

Ds1=['Lan','Nga','Mai','Anh','Ngọc']
Tp1=('Mai','Lan','An','Lê','Liên','Tiến')
# a. Rút ra danh sách những người có tên đồng thời trong Ds1 và Tp1 lưu vào biến Ds2 (Có kiểu danh sách)
Ds2=list(set(Ds1) & set(Tp1))
print(Ds2)
# b. Rút ra danh sách những người có tên trong Ds1 và không có trong Tp1 lưu vào biến Tp2 (Có kiểu tuple)
Tp2=tuple(set(Ds1) - set(Tp1))
print(Tp2)
# c. Rút ra danh sách những người có tên trong Ds1 hoặc có trong Tp1 mà không đồng thời có trong Ds1 và Tp1, lưu vào biến Ds3 (Có kiểu danh sách)
Ds3=list(set(Ds1) ^ set(Tp1))
print(Ds3)
# d. Rút ra danh sách những người có tên trong Ds1 hoặc có trong Tp1, lưu vào biến Ds4 (Có kiểu danh sách)
Ds4=list(set(Ds1) | set(Tp1))
print(Ds4)

