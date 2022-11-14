from math import *

x=float(input())
y=float(input())

def z(x, y):
    if (sqrt(x*x+y*y)>1):
        print("hors cercle")
    elif abs(y)==abs(x):
        print("diagonale")
    elif abs(x)>abs(y):
        print("axe x")
    elif abs(y)>abs(x):
        print("axe y")

z(x,y)
