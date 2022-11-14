def max3entiers(a,b,c):
    if (a>b) and (a>c):
        fin=a
    elif ((b>a) and (b>c)):
        fin=b
    else:
        fin = c
    return fin
