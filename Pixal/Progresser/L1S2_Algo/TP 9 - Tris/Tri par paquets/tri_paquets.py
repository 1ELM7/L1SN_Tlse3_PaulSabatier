def creerListePaquet(m):
    return [[] for i in range(m+1)]

def triPaquet(a,m):  # a est la liste de tuples, m la note maximale (0 étant la minimale)
    b=creerListePaquet(m)
    for i in range (len(a)):
        b[a[i][0]].append(a[i])
    return flat(b)

def flat(b):
    c=[]
    for e in b:
        c.extend(e)
    return c

m=int(input())
a=eval(input())

print(triPaquet(a,m))
