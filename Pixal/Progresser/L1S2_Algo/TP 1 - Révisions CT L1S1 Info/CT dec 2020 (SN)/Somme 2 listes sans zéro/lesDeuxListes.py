def lesDeuxListes(alpha,bravo):
    charlie=[]
    a,b=0,0
    while a<len(alpha) and b<len(bravo):
        if alpha[a]==0:
            a+=1
        elif bravo[b]==0:
            b+=1
        else:
            charlie.append(alpha[a]+bravo[b])
            a+=1
            b+=1

    while a<len(alpha):
        if alpha[a]!=0:
            charlie.append(alpha[a])
        a+=1
    while b<len(bravo):
        if bravo[b]!=0:
            charlie.append(bravo[b])
        b+=1
    return charlie


liste1=eval(input())
liste2=eval(input())
print(lesDeuxListes(liste1,liste2))
