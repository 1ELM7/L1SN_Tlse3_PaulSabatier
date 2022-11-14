def multiple3(n):
    if (n%3==0) and (n%2!=0):
        print("Ce nombre est impair mais est multiple de 3")
    elif (n%2==0):
        print("Ce nombre est pair")
    else:
        print("Ce nombre n est ni pair ni multiple de 3")

n=int(input())
multiple3(n)
