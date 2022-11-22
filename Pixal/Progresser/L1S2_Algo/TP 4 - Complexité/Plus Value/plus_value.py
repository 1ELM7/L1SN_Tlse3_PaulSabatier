def meilleure_plus_value(tab):
    minimum = float('inf')
    plus_value = 0
    for i in range(len(tab)):
        n2 = tab[i]
        if n2 < minimum:
            minimum = n2
        if n2 - minimum > plus_value:
            plus_value = n2 - minimum
    return plus_value
    
tab = eval(input())

print(meilleure_plus_value(tab))
