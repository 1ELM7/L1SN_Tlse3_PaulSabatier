nb = int(input())
# tant qu'on n'a pas décomposé...
while nb != 0:
        # ... on cherche le plus grand carré
    plus_grand_carre = 0
    while plus_grand_carre**2 <= nb:
        plus_grand_carre=plus_grand_carre+1
    # quand on depasse, c'est que c'était le précédent qui était le plus grand carré
    print(plus_grand_carre-1)
    # et on le soustrait à n pour rechercher le prochain plus grand carré
    nb = nb - (plus_grand_carre-1)**2
