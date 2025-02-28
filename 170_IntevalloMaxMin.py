import random

while True:
    min = int(input("MIN: Inserisci un numero compreso tra 1 e 100: "))
    if 1 <= min <= 100:
        break
    else:
        print("Il numero deve essere compreso tra 1 e 100. Riprova.")

while True:
    max = int(input("MAX: Inserisci un altro numero compreso tra 1 e 100: "))
    if 1 <= max <= 100:
        break
    else:
        print("Il numero deve essere compreso tra 1 e 100. Riprova.")

numeriGiusti = []
numeriSbagliati = []
numeriGenerati = []
while True:
    numeri = random.randint(1, 100)
    if numeri < min or numeri > max:
        numeriSbagliati.append(numeri)
        numeriGenerati.append(numeri)
    else:
        numeriGiusti.append(numeri)
        numeriGenerati.append(numeri)
    if len(numeriGiusti) == 10:
        break

print("Numeri prima di soddisfare la condizione:", len(numeriSbagliati) + len(numeriGiusti))
print("Numeri generati:", numeriGenerati)
print("Numeri giusti:", numeriGiusti)
print("Numeri sbagliati:", numeriSbagliati)