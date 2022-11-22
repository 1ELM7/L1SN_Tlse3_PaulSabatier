def longueur(n, nbr):
    if n < 10:
        if n == nbr:
            return 1
        else:
            return 0
    else:
        aux = n%10
        if aux == nbr:
            return 1 + longueur(n//10, nbr)
        return longueur(n//10, nbr)
        
nbr = int(input())
n = int(input())

print(longueur(n, nbr))
