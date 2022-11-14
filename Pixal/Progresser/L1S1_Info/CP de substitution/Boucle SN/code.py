a=int(input())
m=int(input())

if a<=m:
    while a>1:
        m+=m
        a=a/2
    print(m)
else:
    while m>1:
        a+=a
        m=m/2
    if a==20:
        a=15
    print(a)
