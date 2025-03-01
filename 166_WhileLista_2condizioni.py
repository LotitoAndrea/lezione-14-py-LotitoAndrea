lista_numeri = []
risposta = ""
while risposta != "no":
    n = int(input("Inserisci numero: "))
    lista_numeri.append(n)
    risposta = input("Vuoi inserire altri numeri? ")
    if len(lista_numeri) == 5:
        break
print(lista_numeri)