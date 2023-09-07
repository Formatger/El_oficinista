n = int(input("Introduce un numero entero: "))
i = 2
while n % i != 0:
    i = i+1
if i == n:
    print("es primo")
else:
    print("no es primo")
