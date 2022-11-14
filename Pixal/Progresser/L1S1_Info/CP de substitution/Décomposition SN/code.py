n = int(input())
i = 1

while i < n:
    dm=i//10000
    m=(i-(dm*10000))//1000
    c=(i-((dm*10000)+(m*1000)))//100
    d=(i-((dm*10000)+(m*1000)+(c*100)))//10
    u=(i-((dm*10000)+(m*1000)+(c*100)+(d*10)))//1
    if (dm>0):
        if ((dm+m+c+d+u)==(dm*m*c*d*u)):
            print (i)
    elif ((dm==0) and (m!=0)):
        if ((m+c+d+u)==(m*c*d*u)):
            print (i)
    elif ((dm==0) and (m==0) and (c!= 0)):
        if ((c+d+u)==(c*d*u)):
            print (i)
    elif ((dm==0) and (m==0) and (c==0) and (d!=0)):
        if ((d+u)==(d*u)):
            print (i)
    elif ((dm==0) and (m==0) and (c==0) and (d==0)):
        print (i)
    i +=1
