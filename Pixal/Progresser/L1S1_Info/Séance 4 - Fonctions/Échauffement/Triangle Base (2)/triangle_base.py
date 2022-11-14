from lib import dessineLigneC
def triangleBase(n,c):
    while (n!=0):
        dessineLigneC(n,c)
        print("\n")
        n=n-1
