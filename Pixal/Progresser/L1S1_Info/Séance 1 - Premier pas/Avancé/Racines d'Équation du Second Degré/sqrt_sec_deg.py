from math import sqrt 
a=int(input())
b=int(input())
c=int(input())
delta=b**(2)-4*a*c
r1=(-b-sqrt(delta))/(2*a)
r2=(-b+sqrt(delta))/(2*a)
print("Les racines de l'equation sont",r1,"et",r2)
