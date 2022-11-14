from lib import *

def deuxZeros(a,b):
    t=0
    for i in range (a,b+1):
        count=nombreDeZeros(i)
        if count==2:
            t+=1
            print (i)
    if t==0:
        print(0)



a=int(input())
b=int(input())

deuxZeros(a,b)
