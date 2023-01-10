def szo_tisztitas(szo):
    spec = "\'\"+!%/=()~ˇ^˘°˛`˙´,.-?:_;>*>#&@\\{}łŁ$ß÷đĐ[]€"
    spec = [*spec]
    for s in spec:
        szo = "".join(szo.split(s))
    return szo

szo_tisztitas("hogyan?")
szo_tisztitas("'most!'")
szo_tisztitas("?+='s-z-a-v!a,k@$()'")