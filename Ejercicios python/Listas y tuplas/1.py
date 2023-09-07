lista =[]

while True:
    asignatura = input("Introduce un asignatura (escribe \"fin\" para salir):")
    if asignatura == "fin":
        break
    lista.append(asignatura)

print(lista)
