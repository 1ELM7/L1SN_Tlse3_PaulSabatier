def divEucl(a,b):
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

    return (q,r)
    
a = int(input())
b = int(input())
m = int(input())

q,r=divEucl(a+b,m)
print(r)
