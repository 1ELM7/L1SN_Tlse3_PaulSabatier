def nombrePairs(nombre):
    compteur_nombres_pairs=0
    while nombre>0:
        unite=nombre%10
        nombre=nombre//10
        if unite%2==0:
            compteur_nombres_pairs+=1
    
    return compteur_nombres_pairs
