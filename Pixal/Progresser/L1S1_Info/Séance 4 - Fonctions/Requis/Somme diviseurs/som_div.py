def sommeDiviseurs(n):
    somme=0
    i=1
    while i != n+1:
        if (n%i==0):
            somme=somme+i
        i+=1
    return(somme)
