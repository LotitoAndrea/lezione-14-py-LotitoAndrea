import random

numero = int(input("Inserisci un numero: "))
numeriPari = 0
numeriInseriti = []
while numeriPari < numero:
    numeroGenerato = random.randint(40, 90)
    numeriInseriti.append(numeroGenerato)
    if numeroGenerato % 2 == 0:
        numeriPari += 1
print("sono stati prodotti", len(numeriInseriti), "numeri prima di ottenere", numero, "numeri pari")
print("Numeri generati:", numeriInseriti)