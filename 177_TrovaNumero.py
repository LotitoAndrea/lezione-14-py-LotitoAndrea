import random

listaNumeri = []
for i in range(20):
    numeroCasuale = random.randint(1, 100)
    listaNumeri.append(numeroCasuale)
print("Numeri generati:", listaNumeri)

numeroDaTrovare = int(input("Inserisci un numero da trovare: "))
contatore = 0
trovato = False

for n in listaNumeri:
    if n == numeroDaTrovare:
        trovato = True
        break
    contatore += 1

if trovato:
    print("Il numero", numeroDaTrovare, "è stato trovato dopo", contatore, "elementi.")
else:
    print("Il numero", numeroDaTrovare, "non è stato trovato.")