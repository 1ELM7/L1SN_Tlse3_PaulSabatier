def rechercheListeAlgorithmes(methode,liste):
    sort_methode=[]
    for indice in liste:
        (sort,operation,methode_sort)=indice
        if methode_sort==methode:
            sort_methode.append(sort)
    return sort_methode
    
    
    
    

liste=eval(input())
methode=input()
print(rechercheListeAlgorithmes(methode,liste))
