from liste import *

def nombre_occurrences(l, e):
    if est_vide(l):
        return 0
    if tete(l) == e:
        return 1 + nombre_occurrences(queue(l), e)
    return nombre_occurrences(queue(l), e)

element = int(input())    
l = eval(input())

print(nombre_occurrences(l, element))
