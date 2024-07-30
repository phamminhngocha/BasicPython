#T2.2.3(Cách 1-Có tính thời gian thực hiện chương trình)
#Tính B=2+4+6+...+2n
#Cách 1: Sử dụng công thức (Không nên tư duy theo cách này)
import time

n=int(input('n='))

StartTime=time.time()

B=(n+1)*n
print(f"B={B}")

EndTime=time.time()
print("Thời gian thực hiện chương trình theo cách 1: ",EndTime-StartTime," giây")
