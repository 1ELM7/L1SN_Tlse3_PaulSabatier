def est_position_valide(matrice,ligne,colonne):
    if ligne < 0 or colonne < 0:
        return False
    else:
        try:
            valeur = matrice[ligne][colonne]
            return True
        except IndexError:
            return False

#saisie de la matrice liste de listes d'entiers
matrice = eval(input())
#saisie de la liste de coordonnnées
liste_coordonnees=eval(input())
res=[]
#appel de la fonction sur la liste de coordonnées
for (ligne,colonne) in liste_coordonnees:
  res.append(est_position_valide(matrice,ligne,colonne))
print(res)
