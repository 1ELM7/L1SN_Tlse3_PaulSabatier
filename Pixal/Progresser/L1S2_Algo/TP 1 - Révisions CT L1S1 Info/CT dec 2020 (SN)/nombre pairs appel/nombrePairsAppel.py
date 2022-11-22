from lib import *

premier_nombre=int(input())
deuxieme_nombre=int(input())
compteur_double_pair=0

for test in range (premier_nombre,deuxieme_nombre+1):
    if (nombrePairs(test)==2):
        print(test)
        compteur_double_pair+=1

if compteur_double_pair==0:
    print(0)
