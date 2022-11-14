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

def expo_rapide_mod_m(a,b,m):
    r=1
    x=a
    p=b
    v=0
    while p>0:
        p,v=divEucl(p,2)
        if v==1:
            r=(r*x)%m
        x=(x*x)%m
    return r
    
def inverse_mod_m(a, m):
    (g,x,y)=euclide(a,m)
    if(g!=1):
        return "non inversible"
    else:
        v=x%m
        return v

def crypt(M,n,e):
    return(expo_rapide_mod_m(M,e,n))

def decrypt(C,n,d):
    return(expo_rapide_mod_m(C,d,n))

n = int(input())
e = int(input())
d = int(input())
M = int(input())

C = crypt(M, n, e)
print(C)
print(decrypt(C, n, d))
