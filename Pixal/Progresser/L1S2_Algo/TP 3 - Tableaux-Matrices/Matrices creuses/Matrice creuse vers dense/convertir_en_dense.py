def convertir_en_dense(taille,elem,intervalle,position):
    liste = []
    liste_fin = []
    i = 0
    colonne = 0
    while i < len(elem) and i < len(position):
        if position[i] == colonne:
            liste.append(elem[i])
            i += 1
        else:
            liste.append(0)
        if colonne == taille[0]-1 :
            colonne = 0
            liste_fin.append(liste)
            liste = []
        else:
            colonne += 1
    return liste_fin
