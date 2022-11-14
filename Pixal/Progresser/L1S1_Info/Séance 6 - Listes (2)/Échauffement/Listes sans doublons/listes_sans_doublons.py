def doublon(l):
    i=1
    while i<len(l):
        if l[i]==l[i-1]:
            del l[i]
        else:
            i+=1
    return l

liste=eval(input())
print(doublon(liste))
