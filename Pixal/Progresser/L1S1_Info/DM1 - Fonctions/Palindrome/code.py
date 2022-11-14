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
    
count=0

n=int(input())
for i in range (1,n+1):
    if (nombreMiroir(i)==i):
        count+=1

print(count)
