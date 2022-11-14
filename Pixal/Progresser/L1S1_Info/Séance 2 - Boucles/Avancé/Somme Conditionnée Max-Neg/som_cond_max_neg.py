count=0
n=0
p=0
while (p==0):
    n=int(input())
    if (n<0):
        break
    count = count+n
    if (count>1000):
        break

print (count)
