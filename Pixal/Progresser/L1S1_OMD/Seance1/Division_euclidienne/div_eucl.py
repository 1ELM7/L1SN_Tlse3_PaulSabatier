a=int(input())
b=int(input())

q=0
r=a

if (a>=0):
    while (r>=b):
        r=r-b
        q=q+1
else:
    while (r<0):
        r=r+b
        q=q-1

print(q,r)
