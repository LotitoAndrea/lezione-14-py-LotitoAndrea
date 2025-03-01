while True:
    numero1 = float(input("Inserisci un numero: "))
    operatore = input("Inserisci un operatore (+, -, *, /): ")
    numero2 = float(input("Inserisci un altro numero: "))
    if operatore == "+":
        print("Risultato:", numero1 + numero2)
    elif operatore == "-":
        print("Risultato:", numero1 - numero2)
    elif operatore == "*":
        print("Risultato:", numero1 * numero2)
    elif operatore == "/":
        print("Risultato:", numero1 / numero2)
    else:
        print("Operatore non valido")
    continua = input("Vuoi continuare? (si/no): ")
    if continua == "no":
        break