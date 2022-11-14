sp=float(input())
sv=float(input())
pe=float(input())
ve=float(input())

def indicationsPression(sp,sv,pe,ve):
    if (pe>sp) and (ve>sv):
        return "Pression ET volume eleves. Stoppez !"
    elif (sp<pe) and (ve<=sv):
        return "Il faut augmenter le volume"
    elif (sv<ve) and (sp>=pe):
        return "Vous pouvez diminuer le volume"
    else:
        return "Tout va bien !"

print(indicationsPression(sp,sv,pe,ve))
