#definition de la fonction demandee
def liste_occurrences(liste, chaine):
    occ=[]
    for i in range (0,len(liste)):
        if liste[i]==chaine:
            occ.append(i)
    return occ

	
#programme principal	
liste=eval(input())
chaine=input()
	
#a completer : appel de la fonction et affichage du resultat
print(liste_occurrences(liste,chaine))
