from lib import estPremier

def sommePrems(n1,n2):
    count=0
    for i in range (n1+1,n2):
        if (estPremier(i)==True):
            count=count+i
    return count
