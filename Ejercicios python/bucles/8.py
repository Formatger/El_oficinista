n = int(input("Introduce un entero: "))
linea = int()
for i in range(n+1):
    if i % 2 != 0:
        if i == 1:
            linea = f"{i}"
        elif i != 1:
            linea = f"{i} {linea}"
        print(linea)