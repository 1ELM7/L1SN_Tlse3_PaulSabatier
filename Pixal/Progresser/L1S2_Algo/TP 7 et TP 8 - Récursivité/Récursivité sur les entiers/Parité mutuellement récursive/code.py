def pair(n):
    if n == 0:
        return True
    print(n)
    return impaire(n-1)

def impaire(n):
    if n == 0:
        return False
    print(n)
    return pair(n-1)
    
n = int(input())
print(pair(n))
