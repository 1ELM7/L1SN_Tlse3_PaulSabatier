from liste import*

def partitionner_pivot(liste,valeur):
    if est_vide(liste):
        return creer_liste(valeur,liste)
    else:
        if tete(liste)>valeur:
            return creer_liste(valeur,liste)
        else:
            return creer_liste(tete(liste),partitionner_pivot(queue(liste),valeur))

def tri_rapide(liste):
    if est_vide(liste):
         return liste
    else:
        return partitionner_pivot(tri_rapide(queue(liste)),tete(liste))

liste=eval(input())

print(tri_rapide(liste))
