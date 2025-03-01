password = "PippoBaldo101!/"
tentativi = 3
print("Hai 3 tentativi per inserire la password corretta")
while tentativi > 0:
    passwordInserita = input("Inserisci la password: ")
    if passwordInserita == password:
        print("Password corretta")
        break
    else:
        tentativi -= 1
        print("Password errata, tentativi rimasti:", tentativi)
        if tentativi == 0:
            print("Hai esaurito i tentativi")