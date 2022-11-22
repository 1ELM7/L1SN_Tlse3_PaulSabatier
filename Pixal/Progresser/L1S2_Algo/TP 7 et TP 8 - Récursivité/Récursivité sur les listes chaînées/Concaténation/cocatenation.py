from liste import *

def concatener(l1, l2):
    if est_vide(l1):
        return l2
    if est_vide(l2):
        return l1

    return creer_liste(tete(l1), concatener(queue(l1), l2))

l1 = eval(input())
l2 = eval(input())

print(concatener(l1, l2))
