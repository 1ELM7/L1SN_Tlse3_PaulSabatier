from lib import *

def est_minimum_local(matrice,ligne,colonne):
    Min = matrice[ligne][colonne]
    min_local = True
    for i in range(-1,2):
        for j in range(-1,2):
            if est_position_valide(matrice,ligne+i,colonne+j):
                if matrice[ligne+i][colonne+j] < Min:
                    min_local = False
    return min_local

#saisie de la matrice liste de listes d'entiers
matrice = eval(input())                                                                                                                         
#saisie de la liste de coordonnnées                                                                                                             
liste_coordonnees=eval(input())                                                                                                                
res=[]                                                                                                                                          
#appel de la fonction sur la liste de coordonnées                                                                                               
for (ligne,colonne) in liste_coordonnees:                                                                                                       
   res.append(est_minimum_local(matrice,ligne,colonne))                                                                                          
print(res)
