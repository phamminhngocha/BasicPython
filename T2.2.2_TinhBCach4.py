#T2.2.2(Cách 4)
#Tính B=2+4+6+...+2n = 2x1+2x2+2x3+...+2xn
#Cách 2: Sử dụng while với bước nhảy biến chủ trình là 1
n=int(input('n='))
B=0
k=1
while k<=n:
   B+=2*k
   k+=1
print(f"B={B}")
