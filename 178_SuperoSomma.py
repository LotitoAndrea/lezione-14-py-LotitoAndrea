import random

listaNumeri = []
for i in range(20):
    numeroCasuale = random.randint(1, 100)
    listaNumeri.append(numeroCasuale)
print("Numeri generati:", listaNumeri)

numero = int(input("Inserisci un numero: "))
somma = 0
contatore = 0
for n in listaNumeri:
    somma += n
    contatore += 1
    if somma >= numero:
        print("Servono almeno", contatore, "elementi sommati per arrivare a", numero)
        print("Somma:", somma)
        break
    if contatore == len(listaNumeri):
        print("Non ci sono abbastanza elementi per arrivare a", numero)
        break