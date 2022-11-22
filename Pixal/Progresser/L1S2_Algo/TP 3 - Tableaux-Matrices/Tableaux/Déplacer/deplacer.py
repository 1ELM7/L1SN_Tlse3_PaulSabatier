def decaler(tab,i_source,i_destination):
    retenue=0
    if i_source<i_destination:
        for i in range(i_destination-i_source):
            retenue=tab[i_source]
            tab[i_source]=tab[i_source+1]
            tab[i_source+1]=retenue
            i_source=i_source+1
        print(tab)
    elif i_source>i_destination:
        for i in range(i_source-i_destination):
            retenue=tab[i_source]
            tab[i_source]=tab[i_source-1]
            tab[i_source-1]=retenue
            i_source=i_source-1
        print(tab)
    elif i_source==i_destination:
        print(tab)


tab = eval(input())
i_source = int(input())
i_destination = int(input())

decaler(tab,i_source,i_destination)
