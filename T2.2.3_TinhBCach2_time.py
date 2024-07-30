#T2.2.3(Cách 2-Có tính thời gian thực hiện chương trình)
#Tính B=2+4+6+...+2n
#Cách 2: Sử dụng hàm
import time

n=int(input('n='))

StartTime=time.time()

Ds=list(range(2,2*n+1,2))
B=sum(Ds)
print(f"B={B}")

EndTime=time.time()
print("Thời gian thực hiện chương trình theo cách 2: ",EndTime-StartTime," giây")
