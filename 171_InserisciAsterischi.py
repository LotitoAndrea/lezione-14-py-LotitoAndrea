listaCaratteri = []
asterischi = 0
while True:
    carattere = input("Inserisci un carattere: ")
    listaCaratteri.append(carattere)
    if "*" in listaCaratteri:
        asterischi += 1
        if asterischi == 10:
            break
print("Caratteri inseriti:", len(listaCaratteri))