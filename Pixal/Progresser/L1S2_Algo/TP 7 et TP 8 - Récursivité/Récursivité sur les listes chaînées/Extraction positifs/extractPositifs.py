from liste import *

def extraire_positifs(l):
    if est_vide(l):
        return None
    if tete(l) > 0:
        return creer_liste(tete(l), extraire_positifs(queue(l)))
    return extraire_positifs(queue(l))

l = eval(input())
print(extraire_positifs(l))
