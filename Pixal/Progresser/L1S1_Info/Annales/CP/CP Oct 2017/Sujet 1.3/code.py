m=int(input())
n=int(input())
p=int(input())
s= 0
i= m+1
while i < n:
  if (i)%p==0:
    s= s+i
  i= i+1
print(s)
