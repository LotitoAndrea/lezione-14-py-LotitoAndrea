import random

listaNumeri = []
for i in range(20):
    i = random.randint(1, 100)
    listaNumeri.append(i)
print("Numeri generati:", listaNumeri)

numero = int(input("Inserisci un numero: "))
listaPari = []
for n in listaNumeri:
    if len(listaPari) >= numero:
        break
    if n % 2 == 0:
        listaPari.append(n)
print("Numeri pari:", listaPari)