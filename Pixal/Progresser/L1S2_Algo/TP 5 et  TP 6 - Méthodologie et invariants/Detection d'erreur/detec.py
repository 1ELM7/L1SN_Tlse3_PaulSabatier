n = int(input())
a = 0
b = n+1
assert a < b <= n+1 and a**2 <= n < b**2, 'erreur init'
while a != b:
   assert b-a > 0, 'erreur variant'
   t = b-a
   d = (a+b)//2
   if d*d < n:
      a = d
   else:
      b = d
   assert a < b <= n+1 and a**2 <= n <= b**2, 'erreur iteration'
   assert t > b-a, 'boucle infinie'

assert a < b <= n+1 and a**2 <= n < (a+1)**2 , 'erreur objectif'

print (a)
