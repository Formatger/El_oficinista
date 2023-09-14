lista =[]
lista2 = []
while True:
    asignatura = [input("Introduce un asignatura (escribe \"fin\" para salir):"), input("que nota has sacado(fin para salir): ")]
    if asignatura == ["fin", "fin"]:
        break
    lista.append(asignatura)

for i in lista:
    if float(i[1]) < 5:
        lista2.append(i)
print(lista2)