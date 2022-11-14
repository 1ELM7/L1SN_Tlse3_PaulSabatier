def creer_liste(n):
    li=[]
    for i in range(n):
        x=int(input())
        li.append(x)
    return li
def rotation (li):
    if len(li)>1:
        last=li[-1]
        li.insert(0,last)
        del[li[-1]]
    return li

nb = int(input())
li = creer_liste(nb)
print(rotation(li))
