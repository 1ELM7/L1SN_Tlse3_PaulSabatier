def prochain_voisin(ligne,colonne,limite_gauche,limite_droite):
    if colonne >= limite_droite:
        colonne = limite_gauche
        ligne += 1
    else:
        colonne += 1
    return (ligne,colonne)
    
ligne,colonne,limite_gauche,limite_droite = eval(input())
print(prochain_voisin(ligne,colonne,limite_gauche,limite_droite))
