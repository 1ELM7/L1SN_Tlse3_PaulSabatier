def creer_liste (n) :
    li=[]
    for i in range(n):
        e=int(input())
        li.append(e)
    return (li)
nb_element = int(input())
li=creer_liste(nb_element)
print (li)
