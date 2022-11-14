a = int(input())
b = int(input())

def nbreIdiot(a,b):
    for z in range (a,b+1):
        i=z
        m=(-i%1000)//1000;
        c=(i%1000-i%100)//100;
        d=(i%100-i%10)//10;
        u=i%10;
        cube = (m**3)+(c**3)+(d**3)+(u**3)
        if (cube==z):
            print(z)
        z+=1

nbreIdiot(a,b)
