def fibonacci(n):
    # 2 cas d'arrêt 
    if (n == 0): # n = 0 retournant 0
        print ("n= 0 fibonacci= 0")
        return 0
    else: 
        if (n == 1): # n = 1 retournant 1
            print ("n= 1 fibonacci= 1")
            return 1
       
        else: # cas général
            # 2 appels récursifs avec la taille du problème diminuée
            fib = fibonacci(n-1) + fibonacci(n-2)
            print ("n=",n,"fibonacci=",fib)
            return (fib)

def fibo(n):
    assert n>=0, 'erreur domaine de def fibo'
    print(fibonacci(n))

n=int(input())
fibo(n)
