n = int(input("introduce numero entero: "))
lista = range(n)
lista2 = []
for i in range(n):
    if i % 2 != 0:
        lista2.append(i)

impares = [i for i in lista if i % 2 !=0 ]

print(impares)
print(lista2)
