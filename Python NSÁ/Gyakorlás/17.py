év =int(input("Hány éves?"))
if év >= 18:
    print("Tudsz szavazni")
elif év == 17:
    print("Vezetni tanzlhatsz")
elif év == 16:
    print("Tudzs venni lottozó jegyet")
else:
    print("Mehet trükközni vagy kezelni")