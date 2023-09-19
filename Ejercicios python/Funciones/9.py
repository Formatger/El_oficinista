import math as math
lista = [int(input("primer numero")), int(input("segundo numero"))]

def max_divisor():
    resultado1 = math.gcd(lista[0],lista[1])


    return resultado1

def min_multiple():
    resultado2 = (abs(lista[0]*lista[1]))/mcd


    return resultado2

print(max_divisor())
mcd = max_divisor()
mcm = min_multiple()
print(mcm)