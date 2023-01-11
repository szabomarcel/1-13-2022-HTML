s = "Esik eső csendesen, lepereg az ereszen..."
print(s.split())
print(type(s.split()))
print(s.split("e"))
print(s.split("s"))
print("0".join(s.split("e")))

def cserel(s, regi, uj, nyomtatás):
    for i in range(0,len(s)):
        if s[i] == regi:
            s[i] = uj
        return s