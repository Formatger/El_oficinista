lista = input("Introduce numeros separados por coma: ")
lista2 = lista.split(",")
lista2_enteros = [int(cadena) for cadena in lista2]
lista3 = []

def cuadrado():
    for valor in lista2_enteros:
        lista3.append(valor**2)
    return lista3

print(cuadrado())