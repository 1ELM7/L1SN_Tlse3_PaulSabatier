def rechercheListeActeur(lieuRecherche,l):
    final=[]
    for (name,birth,place) in l:
        if lieuRecherche==place:
            final.append(name)
    return final
    
#Récupération des variables 
l=eval(input())
lieuRecherche=input()
print(rechercheListeActeur(lieuRecherche,l))
