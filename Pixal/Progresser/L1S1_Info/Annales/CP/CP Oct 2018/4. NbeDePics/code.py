p=int(input())
n=int(input())

count=0

while (n!=0):
    a=p
    p=n
    n=int(input())
    if (n==0):
        break
    if (a<p) and (p>n):
        count+=1

print(count)
