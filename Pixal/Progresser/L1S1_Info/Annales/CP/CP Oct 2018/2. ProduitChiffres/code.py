n=int(input())
z=n
count=1

while (n>0):
    u=n%10
    n=n//10
    count=count*u
print("le produit des chiffres de", z, "est", count)
