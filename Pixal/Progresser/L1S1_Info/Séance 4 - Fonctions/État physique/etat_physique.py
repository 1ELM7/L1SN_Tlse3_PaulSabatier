def etatPhysique(temp):
    if (temp==0) or (temp==100):
        return "transition"
    elif temp < 0:
        return"solide"
    elif (temp>100):
        return "gaz"
    else:
        return "liquide"
