def puissance_rapide(n,a):
    if n==0:
        return 1
    return  a * puissance_rapide(n-1,a)
    
a=int(input())
n=int(input())
print(puissance_rapide(n,a))
