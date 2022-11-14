c=0
z=1
def dt(c,z):
    while z != 0:
        m = int(input())
        if m == 0:
            print("resultat = ", c)
            z = 0
        elif ((m%2==0) and (m%3==0)):
            c+=1

dt(c,z)
