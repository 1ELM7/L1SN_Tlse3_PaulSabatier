def nombreDeZeros(nombre):
    count=0
    while nombre>0:
        reste=nombre%10
        nombre=nombre//10
        if reste==0:
            count+=1
    return count
