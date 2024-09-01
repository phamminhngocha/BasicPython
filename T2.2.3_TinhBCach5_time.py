#T2.2.3(Cách 5-Có tính thời gian thực hiện chương trình):
#Tính B=2+4+6+...+2n
#Cách 5: Sử dụng for và hàm range()
import time

n=int(input('n='))

StartTime=time.time()

B=0
for k in range(2,2*n+1,2):
    B+=k
print(f"B={B}")

EndTime=time.time()
print("Thời gian thực hiện chương trình theo cách 5: ",EndTime-StartTime," giây")
