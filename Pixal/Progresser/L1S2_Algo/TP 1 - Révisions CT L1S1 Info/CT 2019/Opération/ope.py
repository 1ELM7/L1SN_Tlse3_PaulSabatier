liste = eval(input())
resultat = []
for i in range(len(liste)-1):
    resultat.append(liste[i]-liste[i+1])
print(resultat)
