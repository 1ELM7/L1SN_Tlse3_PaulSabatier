def somme_dense(taille,element,intervalle,position,element1,intervalle1,position1):
    liste=[]
    liste_finale=[]
    i=0
    j=0
    variable=0
    while i<len(element) and i<len(position) and j<len(element1) and j<len(position1):
        if position[i] == variable and position1[j] == variable:
            liste.append(element[i]+element1[j])
            i+=1
            j+=1
        elif position[i]==variable and not position1[j]==variable:
            liste.append(element[i])
            i+=1
        elif position1[j]==variable and not position[i]==variable:
            liste.append(element1[j])
            j+=1
        else:
            liste.append(0)
        if variable==taille[0]-1 :
            variable=0
            liste_finale.append(liste)
            liste=[]
        else:
            variable+=1

    return liste_finale
