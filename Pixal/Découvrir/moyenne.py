def moyenne_num_annee_epreuve(dico,annee,epreuve):
    moyenne = 0.0
    taille = 0
    for cle in dico.keys():
        eleve = dico[cle]
        if eleve[3][2] == annee:
            if epreuve < len(eleve[4]):
                moyenne += eleve[4][epreuve]
                taille += 1
    if taille == 0:
        taille = 1
    return moyenne/taille
