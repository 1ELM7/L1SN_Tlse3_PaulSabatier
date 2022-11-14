from math import *
xa=float(input())
ya=float(input())
xb=float(input())
yb=float(input())

def rayonAB(xa,ya,xb,yb):
    ab=sqrt(((xb-xa)**(2))+((yb-ya)**(2)))
    return (2*pi*ab)

print(rayonAB(xa,ya,xb,yb))
