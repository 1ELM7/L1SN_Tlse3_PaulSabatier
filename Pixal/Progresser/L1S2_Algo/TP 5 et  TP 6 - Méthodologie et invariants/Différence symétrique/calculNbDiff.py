def calculNbDiff(L1,L2):
    nc=0
    for i in L1:
        if i not in L2 :
            nc = nc + 1
    for j in L2:
        if j not in L1 :
            nc = nc + 1
    return nc

L1 = eval(input())
L2=eval(input())
print(calculNbDiff(L1,L2))
