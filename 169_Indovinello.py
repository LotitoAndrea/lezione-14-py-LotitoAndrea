import random

numeroDaIndovinare = random.randint(1, 100)
numero = None
while numero != numeroDaIndovinare:
    numero = int(input("indovina il numero "))
    if numero < numeroDaIndovinare:
        print("il numero da indovinare è più grande")
    elif numero > numeroDaIndovinare:
        print("il numero da indovinare è più piccolo")
    else:
        print("complimenti, hai indovinato!")
        break
print("Arrivederci!")