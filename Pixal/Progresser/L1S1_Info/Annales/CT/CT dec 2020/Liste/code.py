def premiers_indices(liste,nombre):
    case=0
    total = []
    for i in range (0,len(liste)):
        if liste[i-1]==nombre and case<3 and (i-1>=0):
            case+=1
            if (i-1)<0:
                pass
            else:
                total.append(i-1)
    return total
    
liste=eval(input())
n=int(input())

print (premiers_indices(liste,n))
