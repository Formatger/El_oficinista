lista = []
lista_num = list()
while True:
    numero = input("Introduce el numero de la loteria( fin para salir): ")
    if numero == "fin":
        break
    lista.append(numero)

for i in lista:
    lista_num = lista_num + [int(i)]
    # lista_num.append(int(i)) puedo usar esta línea de código, a lo mejor es mas pulida
lista_num.sort(reverse=True)
print(lista_num)