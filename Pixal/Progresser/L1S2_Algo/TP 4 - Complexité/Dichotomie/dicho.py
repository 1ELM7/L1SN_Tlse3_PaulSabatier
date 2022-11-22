def recherche_par_dichotomie ( tab , valeur ) :
    if tab ==[] or tab[0] > valeur :
        return -1
    i , j = 0 , len( tab )
    while i +1 < j :
        m = ( i + j ) //2
        if tab[ m ] <= valeur :
            i = m
        else :
            j = m
    if tab[ i ]== valeur :
        return i
    else :
        return -1

tab=eval(input())
valeur=int(input())
print(recherche_par_dichotomie ( tab , valeur ))
