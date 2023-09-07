lista =[]

while True:
    asignatura = [input("Introduce un asignatura (escribe \"fin\" para salir):"), input("que nota has sacado(fin para salir): ")]
    if asignatura == ["fin", "fin"]:
        break
    lista.append(asignatura)
print(lista)

for i in lista:
    print(f"Yo estudio {i[0]} y he sacado un {i[1]}")