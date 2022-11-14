from utils import *

def num_jour_vers_nom_jour(j):
    jours = ('lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche')
    return jours[j-1]

def jour_de_la_semaine(tuples):
    annee,mois,jour=tuples
    a=annee-1901
    q=a//4
    n=nb_jours_mois_precedent(tuples)
    j=jour
    s=a+q+n+j
    r=(s+1)%7
    return num_jour_vers_nom_jour(r)
