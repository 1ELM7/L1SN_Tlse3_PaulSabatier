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

def euclide(a,b):
    x,y,s,t,u,v=a,b,1,0,0,1
    
    while y>0:
        (q,r) = divEucl(x,y)
        (x,y) = (y,r)
        (s,t,u,v) = (u,v,s-q*u,t-q*v)

    return (x, s, t)


a = int(input())
b = int(input())
(x, s, t) = euclide(a,b)
print([x, s, t])
