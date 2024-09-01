#T2.2.3(Cách 5):
#Tính B=2+4+6+...+2n
#Cách 5: Sử dụng for và hàm range()
n=int(input('n='))
B=0
for k in range(2,2*n+1,2):
    B+=k
print(f"B={B}")
