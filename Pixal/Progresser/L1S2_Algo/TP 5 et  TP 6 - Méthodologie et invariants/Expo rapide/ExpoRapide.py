a=int(input())
b=int(input())
assert b>=0, 'erreur en entrée'
x=a
y=b
z=1 #correction z=0 en z=1
assert a**b == z*(x**y) and y>=0, 'erreur initialisation'
while y!=0:
    if y%2==0:
        y=y//2
        x=x*x
    else:
        y=y-1 # ajout de y=y-1 
        z=z*x
    assert a**b == z*(x**y) and y>=0, 'erreur itération'
assert z==a**b, 'erreur objectif'
print(z)
