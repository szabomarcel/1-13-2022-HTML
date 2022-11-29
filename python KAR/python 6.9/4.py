def napok_hozzadas():
    print(napok_hozzadas("Hétfő",4) == "Péntek")
    print(napok_hozzadas("Kedd",0) == "Kedd")
    print(napok_hozzadas("Kedd",14) == "Kedd")
    print(napok_hozzadas("Hétfő",100) == "Kedd")
print("Írd ki a napot: ")