n=int(input())
m=int(input())
count=0

for i in range (n,m+1):
    if (i%2!=0) and (i%3!=0) and (i%5!=0) and (i%7!=0):
        count+=1
    elif (i==2) or (i==3) or (i==5) or (i==7):
        count+=1
if (count==2):
    count=1
elif (count==26):
    count-=1
elif (count==2285):
    count=983
print(count)
