def division(a,b):
    if a < b:
        return (0,a)
    else:
        q,r = division(a-b,b)
        return (q+1,r)

a = int(input())
b = int(input())
print(division(a,b))
