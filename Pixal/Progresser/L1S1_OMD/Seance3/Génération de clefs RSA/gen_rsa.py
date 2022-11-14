def divEucl(a,b):
    x=a
    y=b
    q=0
    r=a

    if (a>=0):
        while(r>=b):
            r=r-b
            q=q+1
    else:
        while(r<0):
            r=r+b
            q=q-1
    return(q, r)
    
def euclide(a,b):
    x=a
    y=b
    (s,t)=(1,0)
    (u,v)=(0,1)
    while(y>0):
        (q,r)=divEucl(x,y)
        (x,y)=(y,r)
        (s,t,u,v)=(u,v,s-q*u,t-q*v)
    return (x, s, t)
def inverse_mod_m(a, m):
    (g,x,y)=euclide(a,m)
    if(g!=1):
        return "non inversible"
    else:
        v=x%m
        return v
p = int(input())
q = int(input())
e = int(input())
n=p*q
m=(p-1)*(q-1)
d=inverse_mod_m(e,m)
print([n, e, d])
