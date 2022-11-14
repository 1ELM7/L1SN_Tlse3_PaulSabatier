nb=int(input())
chif=int(input())
c=0

while nb>0:
    un=nb%10
    nb=nb//10
    if un==chif:
        c+=1

print(c)
