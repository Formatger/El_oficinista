p = {}
total = 0
while True:
    info = input("Escribe el artículo y su precio (separado por una coma, escribe salir para terminar): ")
    if info == "salir":
        break
    articulo = info.split(",")
    p[articulo[0]] = float(articulo[1])
print(p)
for valor in p:
    print(f"{valor}          {p[valor]}")
    total += p[valor]
print(total)

