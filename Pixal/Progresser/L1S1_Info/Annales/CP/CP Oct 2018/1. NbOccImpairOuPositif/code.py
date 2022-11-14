n=int(input())
count=0

for i in range (1,n+1):
    n=int(input())
    if (n>0) or (n%2!=0):
        count+=1
    i+=1
    
print(count)
