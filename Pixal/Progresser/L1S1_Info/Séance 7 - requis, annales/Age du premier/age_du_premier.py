toutes_les_equipes=eval(input())
total_premier=[]
age_premier=0
for une_equipe in toutes_les_equipes:
    premier_joueur="Z"
    for un_joueur in une_equipe:
        (nom,age)=un_joueur
        if nom<premier_joueur:
            premier_joueur=nom
            age_premier=age
    total_premier.append(age_premier)

print(total_premier)
