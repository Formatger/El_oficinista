import math

precio = float(input("dime prcio con decimales del producto:"))
descomposicion = math.modf(precio)
print(math.trunc(precio))
print(descomposicion)

print(f"El precio es de {descomposicion[1]} euros con {descomposicion[0]} céntimos")

#OTRA MANERA ES HACERLO CON EL find() PERO TENINEDO EN CUENTA QUE EL INPUT VA A SER UNS TRING
