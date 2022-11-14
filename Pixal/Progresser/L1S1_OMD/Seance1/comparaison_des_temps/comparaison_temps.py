import time

def ExpoNaif(a,n):
    r = a
    for i in range (1,n):
        r = a*r
    return(r)

def ExpoRapide(a,n):
    r = 1
    x = a
    p = n
    while (p>0):
        if (p%2 != 0):
            r = r*x
        x = x*x
        p = p//2
    return(r)

def ExpoPython(a,n):
    r = a**n
    return(r)


a = int(input())
n = int(input())

t=time.time()
resultat=ExpoNaif(a,n)
tNaif=time.time()-t

t=time.time()
resultat=ExpoRapide(a,n)
tRapide=time.time()-t

t=time.time()
resultat=ExpoPython(a,n)
tPython=time.time()-t

#pour permettre affichage des arrondis identiques entre vos réponses aux tests et celles de Pixal
print(format(tPython,'.7f'),format(tRapide,'.7f'),format(tNaif,'.7f'))
