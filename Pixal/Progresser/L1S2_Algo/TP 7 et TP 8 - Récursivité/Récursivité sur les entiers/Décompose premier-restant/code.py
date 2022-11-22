def premier_restant(n):
    if n < 10:
        return (n,0)
    else:
        premier,r = premier_restant(n//10)
        return (premier,r*10+n%10)


n = int(input())

print(premier_restant(n))
