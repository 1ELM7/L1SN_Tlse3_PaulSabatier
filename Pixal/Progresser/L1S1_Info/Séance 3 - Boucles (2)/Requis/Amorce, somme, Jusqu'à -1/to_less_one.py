c = 0
c2 = 0
e=0

a=0
b=0

while (e !=-1):
    c2 += 1
    a=b
    b=e
    e = int(input())
    if (e==a+b):
        c+=1

print(c)
