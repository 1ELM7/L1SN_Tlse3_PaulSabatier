def prive_premier_chiffre(n):
    if n < 10:
        return 0
    else:
        return 10*prive_premier_chiffre(n//10)+n%10

n = int(input())
print(prive_premier_chiffre(n))
