from utils import *

def occ_jours_dates(liste):
    tot_jours= [0,0,0,0,0,0,0]
    for j in liste:
        pi=nom_jour_vers_num_jour(jour_de_la_semaine(j))
        annee,mois,jour = j
        for a in range (1,len(tot_jours)+1):
            if a==pi:
                tot_jours[a-1]+=1
    return tot_jours
