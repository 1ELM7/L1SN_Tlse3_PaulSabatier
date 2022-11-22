def tri_bulles(tab):
    j = len(tab)
    while j>0:
        for i in range (len(tab[:j]) -1):
            if tab[i] >tab[i+1]:
                tab[i],tab[i+1] = tab[i+1], tab[i]
        j-=1
    return tab

tab = eval(input())
print(tri_bulles(tab))
