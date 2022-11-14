from utils import est_bissextile

def nb_jours_du_mois(mois,annee):
    if mois==2:
        if est_bissextile(annee)==False:
            tot=28
        else:
            tot = 29
    elif (mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12):
        tot=31
    else:
        tot=30
    
    return tot
