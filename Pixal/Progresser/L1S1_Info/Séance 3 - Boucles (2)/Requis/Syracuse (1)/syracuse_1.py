d = int(input())
c=0
if (d<=0):
    print("Une erreur s'est produite, veuillez entrer un nombre strictement positif s'il vous plait. :)")

while (d != 1):
    
    if (d%2==0):
        d = d/2
    else:
        d = (d*3)+1
    c += 1
    
print(c)
