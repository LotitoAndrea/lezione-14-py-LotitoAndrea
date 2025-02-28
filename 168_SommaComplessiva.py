numero = None
listaNumeri = []
while numero != 0:
    numero = int(input("Inserisci un numero: "))
    listaNumeri.append(numero)
print("somma complessiva:", sum(listaNumeri))
print("Arrivederci!")