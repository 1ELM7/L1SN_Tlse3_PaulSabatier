liste=eval(input())

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

while i<len(liste) : #TODO : CONDITION
    assert len(liste)-i>0,'erreur variant'
    #t introduit pour le test de terminaison
    t=len(liste)-i
    # TODO : ITERATION
    if liste[i]<liste[imin]:
        imin=i
    if liste[i]>liste[imax]:
        imax=i
    i+=1
    assert (imin!= imax 
           and 0<=imin<i 
	   and 0<=imax<i 
	   and liste[imin]==min(liste[0:i]) 
	   and liste[imax]== max(liste[0:i])), \
	   'erreur invariant'
    assert t>len(liste)-i, 'erreur terminaison'

assert (imin != imax
        and i==len(liste) 
	and 0<=imin<i 
	and 0<=imax<i 
	and liste[imin]==min(liste[0:i]) 
	and liste[imax]== max(liste[0:i])), \
	'erreur objectif'

print(imin,imax)
