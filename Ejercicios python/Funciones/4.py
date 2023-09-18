precio = float(input("Introduce precio factura: "))
iva = float(input("Introduce el IVA de la factura:  "))
def calculo(precio, iva):
    if iva == 0:
        iva = 21
    total = (precio*iva) / 100
    total = total + precio
    return total

total = calculo(precio, iva)

print(total)
