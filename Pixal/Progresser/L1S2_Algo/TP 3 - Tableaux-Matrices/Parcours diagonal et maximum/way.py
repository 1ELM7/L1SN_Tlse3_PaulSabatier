carte = eval(input())
depart = eval(input())
chemin = eval(input())

valeur_actuel = carte[depart[0]][depart[1]]

Max = valeur_actuel

for elt in chemin:
    if elt == 'NE':
        depart = (depart[0]-1, depart[1]+1)
    elif elt == 'SE':
        depart = (depart[0]+1, depart[1]+1)
    elif elt == 'SO':
        depart = (depart[0]+1, depart[1]-1)
    elif elt == 'NO':
        depart = (depart[0]-1, depart[1]-1)
    valeur_actuel = carte[depart[0]][depart[1]]
    if valeur_actuel > Max:
        Max = valeur_actuel
print(Max)
