from liste import *
def somme_carres(l):
    if est_vide(l):
        return 0
    return tete(l)**2 + somme_carres(queue(l))
    
l = eval(input())
print(somme_carres(l))
