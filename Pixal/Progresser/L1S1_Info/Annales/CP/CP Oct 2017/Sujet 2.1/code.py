n=int(input())
s=int(input())
count=0

for i in range (1,n):
    p=s
    s=int(input())
    if (s*2==p):
        count+=1
    i+=1
print(count)
