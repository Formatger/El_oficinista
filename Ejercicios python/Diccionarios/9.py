facturas = {}

while True:
    seguir = input("Que quieres hacer? (AÑADIR, LIQUIDAR, TERMINAR): ")
    if seguir == "AÑADIR":
        fact = input("Añade el número de factura y su valor, separado por ':':   ")
        fact2 = fact.split(':')
        facturas[fact2[0]] = fact2[1]
    if seguir == "LIQUIDAR":
        num = input("Escribe el numero de factura: ")
        facturas.pop(num)
    if seguir == "TERMINAR":
        break
for factura, precio in facturas.items():
    print(f"Nº de factura: {factura} - {precio}€ \n")

