x=int(input()) #nombre initial
y=int(input()) #exponentiel de ce nombre

def expoRapide(x,y): #définition de la fonction
    z=x 
    if (x==0): #unique cas particulier
        return 1
    if (x%2==0): #calcul de parité (cas pair)
        for i in range (1,y+1):
            x=x*z
            
        x=x//2
    elif (x%2==1): #calcul de parité (cas impair)
        for i in range (1,y):
            x=x*z
            
    return x

print(expoRapide(x,y))
