#Q1.14

SoChu={1:'Một',2:'Hai',3:'Ba',4:'Bốn',5:'Năm'}
# a. Bổ sung 10: 'Mười' vào cuối từ điển SoChu
SoChu[10] = 'Mười'  # Thêm một cặp key-value mới vào cuối từ điển
print(SoChu)

# Lưu ý: Kiểu Từ điển không có thứ tự nên ta không thể chèn vào một vị trí chính xác như kiểu Danh sách.

# Để đáp ứng yêu cầu b, ta sử dụng toán tử ** (Unpacking) hoặc phương thức update()
# b. Bổ sung 0: 'Không' vào vị trí đầu tiên bên trái từ điển SoChu
# Sử dụng toán tử **:
SoChu1={**{0:"Không"},**SoChu}
print(SoChu)
print(SoChu1)
# Sử dụng phương thức update():
SoChu1={0:"Không"}
SoChu1.update(SoChu)
SoChu=SoChu1
print(SoChu)

# Để đáp ứng yêu cầu c, ta có thể Tạo một từ điển mới, sau đó lần lượt chép các phần tử từ từ điển cũ sang từ điển mới, chèn phần tử cần thêm vào vị trí thích hợp.
# c. Bổ sung 6: 'Sáu' vào sau key 5, trước key 10 trong từ điển SoChu
# Tạo một từ điển mới để lưu trữ kết quả
SoChuMoi = {}
# Chép các phần tử vào từ điển mới và chèn phần tử mới
for key in SoChu:
    SoChuMoi[key] = SoChu[key]
    if key == 5:
        SoChuMoi[6] = 'Sáu'
SoChu=SoChuMoi
print(SoChu)
# d. Xóa key 5 có trong từ điển SoChu
del SoChu[5]
print(SoChu)

# e. Thay giá trị cho key 1 có trong từ điển SoChu thành 'One'
SoChu[1] = 'One'
print(SoChu)
