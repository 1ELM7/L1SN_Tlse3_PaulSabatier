n=int(input())
i=2
somme=0
fib1, fib2 = 1,1
if (n==0) or (n==1):
    fib2=n
else:
    while (fib2<=n):
        if (fib2%2==0):
            somme+=fib2
        tmp=fib2
        fib2=fib1+fib2
        fib1=tmp
        i +=1
            
print(somme)
