from lib import sommeChiffres
n=int(input())
i=1
for i in range (1,n+1):
    p=sommeChiffres(i)
    if i%p==0:
        print(i)
    i+=1
