def entreDeux (u1, u2, total):
    for i in range (u1,u2+1):
        total.append(i)
    return total

def calcul(u1, u2):
    a=u1-u2
    p=u1+u2
    return (a,p)
    

total=[]
liste = eval(input())
j=0
a=len(liste)-1
while j<a:
    u1, u2 = calcul(liste[j], liste[j+1])
    entreDeux(u1, u2, total)
    j=j+2
print(total)
