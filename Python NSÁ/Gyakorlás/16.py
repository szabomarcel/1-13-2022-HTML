eső = input("Esik?")
eső = str.lower(eső)
if eső == "igen":
    szeles = input("Szeles?")
    szeles = str.lower("szeles")
    if szeles == "yes":
        print("Szeles akkor kellene egy esernyő")
    else:
        print("Vegyünk egy esernyőt")
else:
    print("Élveze a napot")