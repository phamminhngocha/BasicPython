#T2.2.1:
Tuoi = int(input("Nhập tuổi của bạn: "))
if 0 < tuoi < 6:
    print("Bạn là trẻ em.")
elif 6 <= tuoi < 10:
    print("Bạn là nhi đồng.")
elif 10 <= tuoi < 18:
    print("Bạn là thiếu nhi.")
elif 18 <= tuoi < 40:
    print("Bạn là thanh niên.")
elif 40 <= tuoi < 65:
    print("Bạn là trung niên.")
else:
    print("Bạn là người cao tuổi.")
