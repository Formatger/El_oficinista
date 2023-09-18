num = input("Escribe un número entero: ")
num = int(num)

def factorial(numero):
    resultado=1
    for valor in range(1, numero + 1):
        resultado  = valor * resultado
    return resultado

print(factorial(num))
