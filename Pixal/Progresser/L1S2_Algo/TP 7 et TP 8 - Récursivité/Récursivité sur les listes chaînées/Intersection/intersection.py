from liste import *

def elements_communs(l1, l2):
    if est_vide(l1) or est_vide(l2):
        return None
    if tete(l1) == tete(l2):
        return creer_liste(tete(l1), elements_communs(queue(l1), queue(l2)))
    if tete(l1) < tete(l2):
        return elements_communs(queue(l1), l2)
    return elements_communs(l1, queue(l2))

l1, l2 = eval(input()), eval(input())

print(elements_communs(l1, l2))
