#T2.2.3(Cách 2)
#Tính B=2+4+6+...+2n
#Cách 2: Sử dụng hàm
n=int(input('n='))
Ds=list(range(2,2*n+1,2))
B=sum(Ds)
print(f"B={B}")
