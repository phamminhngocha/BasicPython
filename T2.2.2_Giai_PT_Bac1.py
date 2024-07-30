#T2.2.2-Giải phương trình bậc 1: ax+b=0
a=float(input('a='))
b=float(input('b='))
if a!=0:
    x=-b/a
    print(f"Phương trình có nghiệm duy nhất x=",x)
else:
    if b!=0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình vô số nghiệm")

