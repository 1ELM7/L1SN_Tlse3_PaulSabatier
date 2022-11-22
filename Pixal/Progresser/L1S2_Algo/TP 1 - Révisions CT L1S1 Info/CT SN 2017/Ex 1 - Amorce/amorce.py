a=int(input())
b=int(input())
z=int(input())
somme=0

while (z != -1):
    y=z
    z=int(input())
    if ((y==a) and (z==b)):
        somme+=1

print(somme)
