def somme_carres(n):
    if n==0:
        return 0
    else:
        return (n**2+somme_carres(n-1))

n=int(input())
print(somme_carres(n))
