a=int(input())
b=int(input())
c=int(input())
maxi=0
def maxx(a,b,c):
    if a>b:
        maxi=a
    else:
        maxi=b
    if maxi<c:
        maxi=c
    return maxi

print(maxx(a,b,c))
