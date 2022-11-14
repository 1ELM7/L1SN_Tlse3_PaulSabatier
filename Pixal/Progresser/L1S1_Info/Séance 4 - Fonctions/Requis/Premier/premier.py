def premier(n):
    if (n==0) or (n==1):
        return False
    elif (n==2):
        return True
    else:
        i = 2
        while i<n:
            if (n%i==0):
                return False
            i+=1
        return True
