from math import *
carte=eval(input())
resume=eval(input())
client=int(input())

def addition(carte,resume,client):
    count=0
    for (num,table,plat) in resume: 
        if num==client:
            sa_table=table
            for (pl,prix) in carte:
                if plat==pl:
                    sans_reduc=prix
            for (num,table,plat) in resume:
                if table==sa_table:
                    count+=1
            if count>=4 and count<6:
                avec_reduc=sans_reduc*0.9
            elif count>=6 and count<10:
                avec_reduc=sans_reduc*0.8
            elif count<4:
                avec_reduc=sans_reduc
            else:
                avec_reduc=sans_reduc*0.7
    
    return floor(avec_reduc)
    

print(addition(carte,resume,client))
