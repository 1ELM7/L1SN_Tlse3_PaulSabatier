def est_bissextile(a):
    if (a%4==0 and a%100!=0) or (a%400==0):
        b= True
    else:
        b=False
    return b
