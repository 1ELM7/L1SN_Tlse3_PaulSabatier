from lib import *
def liste_minima_locaux(matrice):
    minimums = []
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if est_minimum_local(matrice,i,j):
                minimums.append((i,j))
    return minimums 
matrice = eval(input())

print(liste_minima_locaux(matrice))
