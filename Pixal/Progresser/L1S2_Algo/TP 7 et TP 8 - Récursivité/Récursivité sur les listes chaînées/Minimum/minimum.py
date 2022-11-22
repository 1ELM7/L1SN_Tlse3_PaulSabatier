from liste import *

def minimum(l):
    if est_vide(queue(l)):
        return tete(l)
    Min = minimum(queue(l))
    if tete(l) < Min:
        return tete(l)
    return Min
    
    

l = eval(input())

print(minimum(l))
