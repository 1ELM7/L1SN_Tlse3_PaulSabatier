def sommeDiviseurs(n):
    somme=0
    i=1
    while i != n:
        if (n%i==0):
            somme=somme+i
        i+=1
    return(somme)

n=int(input())

for i in range (1,n):
    if sommeDiviseurs(i)==i:
        print(i)
