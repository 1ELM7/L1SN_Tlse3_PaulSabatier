from liste import *

def inserer_element(l, i, val):
    if est_vide(l):
        return creer_liste(val, None)
    if i > 0:
        return creer_liste(tete(l), inserer_element(queue(l), i-1, val))
    return creer_liste(val, l)
    
l = eval(input())
i = int(input())
val = int(input())

print(inserer_element(l, i, val))
