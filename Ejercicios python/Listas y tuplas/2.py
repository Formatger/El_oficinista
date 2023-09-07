lista =[]

while True:
    asignatura = input("Introduce un asignatura (escribe \"fin\" para salir):")
    if asignatura == "fin":
        break
    lista.append(asignatura)

for i in range(len(lista)):
    print(f"Yo estudio {lista[i]}")

for i in lista:
    print(f"Yo estudio {i}")