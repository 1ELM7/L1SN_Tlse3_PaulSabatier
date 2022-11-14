a=int(input())
b=int(input())
c=int(input())

if (a<b):
    if ((c>=a)and(c<=b)):
        print("Le troisieme entier lu ", c, "est dans l'intervalle ", a, b)
    else:
        print("Le troisieme entier lu ", c, "est hors de l'intervalle ", a, b)
else:    
    if ((c>=b)and(c<=a)):
        print("Le troisieme entier lu ", c, "est dans l'intervalle ", b, a)
    else:
        print("Le troisieme entier lu ", c, "est hors de l'intervalle ", b, a)
