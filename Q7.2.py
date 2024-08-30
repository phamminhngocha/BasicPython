#Q7.2
def Ham01(x):
    if x <= 0:
        return False
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i    
    return s == x
n=int(input('Nhập n='))
if Ham01(n):
    print(f"{n } là ???.")
else:
    print(f"{n } không là ???.")














