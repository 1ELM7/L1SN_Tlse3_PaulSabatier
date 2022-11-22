from liste import *

def inserer_dans_liste_triee(liste, val):
    if est_vide(liste):
        return creer_liste(val, None)
    if tete(liste) > val:
        return creer_liste(val, liste)
    return creer_liste(tete(liste), inserer_dans_liste_triee(queue(liste), val))
    
def tri_insertion(liste):
    if est_vide(liste):
        return creer_liste_vide()
    return inserer_dans_liste_triee(tri_insertion(queue(liste)), tete(liste))
    
l = eval(input())
print(tri_insertion(l))
