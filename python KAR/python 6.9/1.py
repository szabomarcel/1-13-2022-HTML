def fordulj_orajarasi_iranyba(teszt):
    teszt = teszt.lower()
    data = ""
    if teszt == "d":
        data = "Nyugat"
    elif teszt == "é": 
        data ="Dél"
    elif teszt == "k":
        data = "Észak"
    elif teszt == "ny":
        data = "Kelet"
    else:    
        következő = None

    return data


print("Írja ki egy éghtájat:(É, K, Ny, K)", teszt(input("Írd be a jelenlegi égtájat: ")).lower)