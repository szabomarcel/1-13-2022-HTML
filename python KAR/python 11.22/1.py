def rule(start,stop,step):
    if (start < stop and step > 0) or (start > stop and step < 0):
        print(list(range(start, stop, step)))
    else:
        print("A paraméterek nem megfelelöek")
rule(10, 0, -2)