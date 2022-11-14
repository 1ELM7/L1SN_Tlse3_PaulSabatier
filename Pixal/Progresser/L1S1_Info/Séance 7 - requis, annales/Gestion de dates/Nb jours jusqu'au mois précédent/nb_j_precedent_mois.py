from utils import nb_jours_du_mois

def nb_jours_mois_precedent(tuples):
    tot=0
    annee,mois,jour = tuples
    if mois==1:
        tot=0
    else:
        for j in range (1,mois):
                tot+=nb_jours_du_mois(j,annee)
        tot+=jour-1
    return tot
