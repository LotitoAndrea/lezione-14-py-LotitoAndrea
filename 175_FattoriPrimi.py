numero = int(input("Inserisci un numero: "))
numeroOriginale = numero
fattoriPrimi = []
for i in range(2, numeroOriginale + 1):
    while numero % i == 0:
        fattoriPrimi.append(i)
        numero = numero // i
print("Fattori primi:", fattoriPrimi)