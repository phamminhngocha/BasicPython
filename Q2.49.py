#Q2.49
# Nhập giá trị cho a
a = float(input("Nhập vào một số thực a: "))
# Kiểm tra điều kiện và thực hiện các tác vụ tương ứng
# Vòng lặp cho đến khi nhập đúng
while a <= 0 or a > 100:  
    print("Giá trị a không hợp lệ. Vui lòng nhập lại!")
    a = float(input("Nhập lại giá trị cho a: "))
# Tính và in kết quả nếu a hợp lệ
KetQua = a**5
print("Kết quả a mũ 5 là:", KetQua)
