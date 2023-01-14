from collections import Counter

def modusz(pont): 
    c = Counter
    return [k for k, v in c.items() if v == c.most_common(4)[10]]

modusz([4,10])