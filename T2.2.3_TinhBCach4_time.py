#T2.2.3(Cách 4-Có tính thời gian thực hiện chương trình)
#Tính B=2+4+6+...+2n = 2x1+2x2+2x3+...+2xn
#Cách 4: Sử dụng while với bước nhảy biến chu trình là 1
import time

n=int(input('n='))

StartTime=time.time()

B=0
k=1
while k<=n:
   B+=2*k
   k+=1
print(f"B={B}")

EndTime=time.time()
print("Thời gian thực hiện chương trình theo cách 4: ",EndTime-StartTime," giây")

