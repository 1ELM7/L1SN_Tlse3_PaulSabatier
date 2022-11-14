n=int(input())
i=2
fib1, fib2 = 1,1
if (n==0) or (n==1):
    fib2=n
else:
    while (i<n):
        tmp=fib2
        fib2=fib1+fib2
        fib1=tmp
        i +=1
print(fib2)
