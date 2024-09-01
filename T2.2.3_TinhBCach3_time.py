#T2.2.3(Cách 3-Có tính thời gian thực hiện chương trình):
#Tính B=2+4+6+...+2n
#Cách 3: Sử dụng while
import time

n=int(input('n='))

StartTime=time.time()

B=0
k=2
while k<=2*n:
   B+=k
   k+=2
print(f"B={B}")

EndTime=time.time()
print("Thời gian thực hiện chương trình theo cách 3: ",EndTime-StartTime," giây")
