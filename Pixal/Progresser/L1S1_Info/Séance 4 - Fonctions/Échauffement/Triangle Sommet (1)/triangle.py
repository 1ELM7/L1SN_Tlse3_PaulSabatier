from lib import dessineLigneC

def triangleSommet(n,c):
    for i in range (1,n+1):
        dessineLigneC(i,c)
        print("\n")
