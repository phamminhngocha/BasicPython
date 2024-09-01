#T2.2.3(Cách 3):
#Tính B=2+4+6+...+2n
#Cách 3: Sử dụng while
n=int(input('n='))
B=0
k=2
while k<=2*n:
   B+=k
   k+=2
print(f"B={B}")
