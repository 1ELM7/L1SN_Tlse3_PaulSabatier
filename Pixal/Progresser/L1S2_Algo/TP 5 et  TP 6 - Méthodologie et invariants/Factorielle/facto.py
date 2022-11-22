import math
n=int(input())
factorielle=1
i=1

while i <= n:
    assert n-i >=0, 'pb variant'
    factorielle*=i
    assert factorielle == math.factorial(i), 'pb invariant'
    i+=1

print(factorielle)
