def longueur(n):
    if n < 10:
        return 1
    else:
        return 1 + longueur(n//10)
        
n = int(input())
print(longueur(n))
