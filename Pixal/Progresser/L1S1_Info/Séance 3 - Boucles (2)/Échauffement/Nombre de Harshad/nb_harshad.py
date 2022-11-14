n = int(input())
i = n
count = 0

while (i>0):
    r=i%10
    i=i//10
    count=count+r

r=n/count
if (r%2==0)or (r%2==1):
    print("oui")
else:
    print("non")
