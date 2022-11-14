def amorce(antépénultième,av_dernier,dernier):
    count = 0
    while dernier != -1:
        if antépénultième == dernier-av_dernier or antépénultième==av_dernier-dernier:
            count+=1
        antépénultième = av_dernier
        av_dernier = dernier
        dernier = int(input())
    return count

premier=int(input())
second=int(input())
troisième=int(input())
print(amorce(premier,second,troisième)) #Pour les trois premières valeures
