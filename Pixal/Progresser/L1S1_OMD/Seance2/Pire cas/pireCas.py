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
    x,y,s,t,u,v,count=a,b,1,0,0,1,0
    
    while y>0:
        (q,r) = divEucl(x,y)
        count+=1
        (x,y) = (y,r)
        (s,t,u,v) = (u,v,s-q*u,t-q*v)

    return count


def pireCas(n):
    maxi = 0
    for i in range (1,n):
        temp = euclide(n,i)
        if temp>maxi:
            maxi=temp
            plus=i
            
    return maxi

n=int(input())
print(pireCas(n))
