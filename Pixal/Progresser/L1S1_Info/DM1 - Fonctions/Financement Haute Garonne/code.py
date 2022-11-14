age=int(input())
salaire=int(input())
statut=str(input())
handi=str(input())

def droitFinancement(age, salaire, statut, handi):
    if (statut=='incapable'):
        return "Pas de droit a un financement"
    elif (age<18) and (statut!='emancipe'):
        return "Financement autorise percu par les parents du candidat"
    elif ((age>=18) and (salaire<1500)) or ((age>=18) and (handi=='oui')) or (statut=='emancipe'):
        return "Financement autorise percu par le candidat"
    else:
        return "Pas de droit a un financement"

print(droitFinancement(age, salaire, statut, handi))
