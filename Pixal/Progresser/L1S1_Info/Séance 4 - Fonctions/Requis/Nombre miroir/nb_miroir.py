def nombreMiroir(a):
    a = str(a)
    liste= []
    for i in a:
        liste.append(i)
    liste.reverse()
    stri=""
    for i in liste:
        stri+=i
    return int(stri)
