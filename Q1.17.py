#Q1.17 

Tuoi = 25  # Giả sử giá trị của biến Tuoi
# a. Kiểm tra giá trị trong biến Tuoi có nằm trong đoạn [15,30] hay không?
print(15 <= Tuoi <= 30)
# b. Kiểm tra giá trị trong biến Tuoi có nằm ngoài khoảng (20,30) hay không?
print(not (20 < Tuoi < 30))
# c. Kiểm tra giá trị trong biến Tuoi có nằm trong đoạn [10,20] hoặc trong đoạn [30,40] hay không?
print((10 <= Tuoi <= 20) or (30 <= Tuoi <= 40))
# d. Kiểm tra giá trị trong biến Tuoi có nằm ngoài đoạn [10,20] đồng thời nằm ngoài đoạn [30,40] hay không?
print(not (10 <= Tuoi <= 20) and not (30 <= Tuoi <= 40))

Password = "Ab1*de2"  # Giả sử giá trị của biến Password
# e. Kiểm tra độ dài chuỗi ký tự có trong biến Password có nằm trong đoạn [8,15] hay không?
print(8 <= len(Password) <= 15)
# f. Kiểm tra chuỗi ký tự có trong biến Password chỉ chứa các chữ cái hay không?
print(Password.isalpha())
# g. Kiểm tra chuỗi ký tự có trong biến Password chỉ chứa các chữ cái và là chữ thường hay không?
print(Password.islower())
# h. Kiểm tra chuỗi ký tự có trong biến Password chỉ chứa các chữ cái và là chữ HOA hay không?
print(Password.isupper())
# i. Kiểm tra chuỗi ký tự có trong biến Password chỉ chứa các chữ cái và ký tự đặc biệt hay không?
import re
    # Định nghĩa biểu thức chính quy chỉ cho phép chữ cái và ký tự đặc biệt
Pattern = r'^[A-Za-z!@#$%^&*(),.?":{}|<>]+$'
print(re.match(Pattern, Password)  is not None)
# j. Kiểm tra chuỗi ký tự có trong biến Password chỉ chứa các chữ cái và chữ số hay không?
print(Password.isalnum())

# k. Kiểm tra chuỗi ký tự có trong biến Password có chứa các chữ cái (Có cả chữ hoa và chữ thường), chữ số và không chứa ký tự đặc biệt?
import re
print(re.match("^[a-zA-Z0-9]+$", Password) is not None)

# l. Kiểm tra chuỗi ký tự có trong biến Password có chứa ít nhất một chữ cái hoa, một chữ cái thường, một chữ số, một ký tự đặc biệt và có độ dài k ký tự hay không?
k=7
import re
    # Định nghĩa biểu thức chính quy chỉ cho phép chữ cái và ký tự đặc biệt
Pattern = f"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{{{k}}}$"
print(re.match(Pattern, Password) is not None)
