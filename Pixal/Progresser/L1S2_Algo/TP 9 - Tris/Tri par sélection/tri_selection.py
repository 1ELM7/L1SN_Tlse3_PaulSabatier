from liste import*
def extraire_minimum(liste,valeur):
    if est_vide(liste):
        return creer_liste(valeur,liste)
    else:
        if tete(liste)>valeur:
            return creer_liste(valeur,liste)
        else:
            return creer_liste(tete(liste),extraire_minimum(queue(liste),valeur))

def tri_selection(liste):
    if est_vide(liste):
         return liste
    else:
        return extraire_minimum(tri_selection(queue(liste)),tete(liste))

liste=eval(input())

print(tri_selection(liste))
