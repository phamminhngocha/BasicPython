#Q7.1
import random
# ???
t = 1000000000  
# ???
f = "Numbers.txt"
# ???
with open(f, 'w') as file:
    # ???
    for _ in range(t):
        r = random.randint(1, 1000000) 
        file.write(f"{r}\n")
print(f"{t} giá trị ??? và lưu vào file {f}.")














