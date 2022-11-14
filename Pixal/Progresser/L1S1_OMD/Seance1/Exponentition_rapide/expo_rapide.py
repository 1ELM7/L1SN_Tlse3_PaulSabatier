a=int(input())
n=int(input())

r=1
x=a
p=n

while (p>0):
    if (p%2!=0):
        r=r*x
    x=x*x
    p=p//2

print(r)
