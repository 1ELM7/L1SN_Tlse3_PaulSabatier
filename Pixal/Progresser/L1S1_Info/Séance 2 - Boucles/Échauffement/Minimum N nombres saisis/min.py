y=int(input())
c=0
x=0
z1=(int(input()))
while (c!=(y-1)):
    c+=1
    z=(int(input()))
    if (z1<z):
        x=z1
    else:
        x=z
if (x==0):
    x=1
print("minimum =", x)
