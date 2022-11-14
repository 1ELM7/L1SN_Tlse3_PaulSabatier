def sommeCubesPairs(n1, n2):
    somme=0
    for i in range (n1,n2+1):
        if (i%2==0):
            somme=somme+(i**3)
    return somme
