n=int(input())
somme = 0
z=-1

for i in range (1,n+1):
    y=z
    z=int(input())
    if (z%2!=0) and (z==y+1):
        somme+=1
    i+=1


print(somme)
