def sans_zero ( liste1 , liste2 ) :
    i1 , i2 = 0,0
    liste3 = []
    while i1<len( liste1 ) and i2<len( liste2 ) :
        if liste1 [ i1 ] == 0 :
            i1 = i1 + 1
        elif liste2 [ i2 ] == 0 :
            i2 = i2 + 1
        else :
            liste3 .append( liste1 [ i1]+ liste2 [ i2 ])
            i1 = i1 + 1
            i2 = i2 + 1
    return liste3
    
premiere_liste=eval(input())
deuxieme_liste=eval(input())
print(sans_zero(premiere_liste,deuxieme_liste))
