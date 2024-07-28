#Q1.12

TenKhoa=('Khoa Hệ thống thông tin kinh tế')
TpTenKhoa=tuple(TenKhoa.split(' '))# a. Chuyển chuỗi ký tự TenKhoa về tuple TpTenKhoa, sao cho mỗi từ là một phần tử của tuple.
print(TpTenKhoa[0]) # b. Lấy 1 phần tử bên trái của tuple TpTenKhoa
print(TpTenKhoa[-1]) # c. Lấy 1 phần tử bên phải của tuple TpTenKhoa
print(TpTenKhoa[:3]) # d. Lấy 3 phần tử bên trái của tuple TpTenKhoa
print(TpTenKhoa[-6:]) # e. Lấy 6 phần tử bên phải của tuple TpTenKhoa
print(TpTenKhoa[1:5]) # f. Lấy từ phần tử thứ 2 đến phần tử thứ 5 có trong tuple TpTenKhoa (Tính từ trái qua phải)
print(TpTenKhoa[-4:-2]) # g. Lấy từ phần tử thứ 3 đến phần tử thứ 4 có trong tuple TpTenKhoa (Tính từ phải qua trái)
print(TpTenKhoa[3:]) # h. Lấy từ phần tử thứ 4 đến phần tử cuối cùng có trong tuple TpTenKhoa (Tính từ trái qua phải)
print(TpTenKhoa[:-4]) # i. Lấy từ phần tử thứ 5 đến phần tử cuối cùng có trong tuple TpTenKhoa (Tính từ phải qua trái)
print(TpTenKhoa[::2]) # j. Lấy các phần tử ở các vị trí chẵn có trong tuple TpTenKhoa
TpTenKhoa2=TpTenKhoa[::-1] # k. Tạo tuple chứa các phần tử có trật tự đảo ngược với tuple TpTenKhoa, lưu vào tuple TpTenKhoa2
print(TpTenKhoa2)
print(TpTenKhoa2[:4]) # l. Lấy 4 phần tử đầu tiên bên trái của TpTenKhoa2
