import time

#lignes specifiques pour tracer une courbe
import matplotlib as mpl
#rajouter la ligne suivante pour repl.it (pas PIXAL)
#mpl.use('Agg')
import matplotlib.pyplot as plt
fig = plt.figure()
#et uniquement sur pixal (pas sur repl.it)
ax = fig.add_subplot(111)

def dve(a, b):
    r=a
    q=0
    if r > 0:
        while r >= b:
            r = r-b
            q += 1
    else:
        while r < 0:
            r = r+b
            q -= 1
    return (q, r)

def expoRapide(a, p):
    r=1
    x=a
    while p>0:
        (p,e) = dve(p, 2)
        if e > 0:
            r=r*x
        x = x*x
    return r
    
def expoNaive(n,p):
    nb = 1
    for i in range(p):
        nb = nb * a 
    
    return nb

def expoPython(a,n):
    r = a**n
    return(r)
    
def temps(fct, a, p):
    t = time.time()
    res = fct(a, p)
    actu = time.time()
    return actu - t

a = int(input())
n = int(input())


temps1=[0]*n
temps2=[0]*n
temps3=[0]*n

x=[0]*n
for i in range(n):
    x[i]=i+1

for i in range(n+1):
    temps1[i-1] = temps(expoPython, a, i)
    temps2[i-1] = temps(expoNaive, a, i)
    temps3[i-1] = temps(expoRapide, a, i)


#lignes pour tracer les courbes 
plt.plot(x,temps1,'r')
plt.plot(x,temps2,'b')
plt.plot(x,temps3,'g')

plt.show()

# pour PIXAL
returnFig(fig)
#remplacer la derniere ligne par la suivante pour les tests sur repl.it
#fig.savefig('https://static-items.algorea.org/files/checkouts/591739407/OMD01/comparaisonN/essai.png')
#vous pourrez meme recuperer le fichier de la courbe
