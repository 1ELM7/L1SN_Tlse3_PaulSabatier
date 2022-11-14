from lib import dessineLigneCSep


def pyramide(n,c):
    s=" "
    k=n
    for i in range (1,n+1):
        k=k-1
        for j in range (1,k+1):
            print(" ",end="")
        dessineLigneCSep(i,c,s)
        print(" ")
