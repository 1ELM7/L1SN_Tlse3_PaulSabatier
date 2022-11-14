def creation(nb):
    li=[]
    while (nb>0):
        u=nb%10
        nb=nb//10
        li.append(u)
    li.reverse()
    if (li == []):
        li.append(0)
    return(li)
    
enp = int(input())   #enp pour entier naturel positif 
print(creation(enp))
