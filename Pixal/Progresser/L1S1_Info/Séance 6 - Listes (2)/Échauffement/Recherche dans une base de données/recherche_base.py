def rechercheDate(nomRecherche,liste):
    for (nom,dateNaissance,lieuNaissance) in liste: 
        if nom==nomRecherche:
            return dateNaissance
    return ("Absent de la base")
    
l=eval(input())
nomRech=input()
print(rechercheDate(nomRech,l))
