#Q1.11

Ds=[1,2,3,4,5,'Một','Hai','Ba','Bốn','Năm']
print(Ds[0])  # a. Lấy 1 phần tử bên trái của danh sách Ds
print(Ds[-1])  # b. Lấy 1 phần tử bên phải của danh sách Ds
print(Ds[:3])  # c. Lấy 3 phần tử bên trái của danh sách Ds
print(Ds[-5:]) # d. Lấy 5 phần tử bên phải của danh sách Ds
print(Ds[1:6]) # e. Lấy từ phần tử thứ 2 đến phần tử thứ 6 có trong danh sách Ds (Tính từ trái qua phải)
print(Ds[-6:-1]) # f. Lấy từ phần tử thứ 2 đến phần tử thứ 6 có trong danh sách Ds (Tính từ phải qua trái)
print(Ds[4:]) # g. Lấy từ phần tử thứ 5 đến phần tử cuối cùng có trong danh sách Ds (Tính từ trái qua phải)
print(Ds[:-6]) # h. Lấy từ phần tử thứ 7 đến phần tử cuối cùng có trong danh sách Ds (Tính từ phải qua trái)
print(Ds.insert(5,'6')# i. Chèn giá trị 6 vào sau phần từ có chỉ mục 4 của danh sách Ds
print(Ds[1::2]) # j. Lấy các phần tử ở các vị trí chẵn có trong danh sách Ds
Ds2=Ds[::-1]# k. Tạo danh sách chứa các phần tử có trật tự đảo ngược với danh sách Ds, lưu vào biến danh sách Ds2
print(Ds2)
