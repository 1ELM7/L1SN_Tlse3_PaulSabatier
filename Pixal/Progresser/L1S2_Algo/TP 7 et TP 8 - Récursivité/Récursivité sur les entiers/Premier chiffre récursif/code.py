def premier_chiffre(n):
    if n < 10:
        return n
    else:
        return premier_chiffre(n//10)
        
n = int(input())
print(premier_chiffre(n))
