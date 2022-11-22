liste=eval(input())

def deux_plus_grands(liste):
    # TODO : INITIALISATION
    if liste[0]<liste[1]:
        imin=0
        imax=1
    else:
        imin=1
        imax=0
    i=2
    assert (imin!=imax 
       and 0<=imin<i 
       and 0<=imax<i 
       and liste[imin]==min(liste[0:i]) 
       and liste[imax]== max(liste[0:i])), \
       'erreur initialisation'
    
    while i<len(liste) :
        assert len(liste)-i>0,'erreur variant'
        if liste[i]>liste[imax]:
            imin=imax
            imax=i
        elif liste[imin]<liste[i] and liste[imax]>=liste[i]:
            imin=i
        i+=1
    
    return (liste[imax],liste[imin])

print(deux_plus_grands(liste))
