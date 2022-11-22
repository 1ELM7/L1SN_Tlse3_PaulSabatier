def deux_maxima(tab):
    if tab[0]>tab[1]:
        max1 = tab[0]
        max2 = tab[1]
    else:
        max1=tab[1]
        max2=tab[0]
    for i in range (2,len(tab)):
        val = tab[i]
        if val>max1:
            max2=max1
            max1=val
        elif val > max2:
            max2 = val
    return (max1, max2)
    
def somme_maximale(oui):
    a, b = oui
    maximum = a+b
    return maximum

tab = eval(input())
print(somme_maximale(deux_maxima(tab)))
