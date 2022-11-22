def derniers_indices(liste_entree):
    longueur = len(liste_entree)-1
    derniers_impairs=[]
    count=0
    while longueur>=0:
        if count < 3 and (liste_entree[longueur]%2==1):
            count+=1
            derniers_impairs.append(longueur)
        longueur-=1
        
    return derniers_impairs
    
liste=eval(input())
print (derniers_indices(liste))
