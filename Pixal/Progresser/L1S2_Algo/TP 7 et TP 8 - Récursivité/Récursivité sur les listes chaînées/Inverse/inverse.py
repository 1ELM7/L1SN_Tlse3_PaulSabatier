from liste import *

def inverser_rec(liste,liste_inverse):
    if est_vide(liste):
        return liste_inverse
    liste_inverse = creer_liste(tete(liste), liste_inverse)
    return inverser_rec(queue(liste),liste_inverse)

def inverser(liste):
    return inverser_rec(liste,creer_liste_vide())

l = eval(input())
print(inverser(l))
