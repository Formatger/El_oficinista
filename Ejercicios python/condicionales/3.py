n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

if n2 == 0:
    print("Error, no se puede dividir por 0")
elif n2 != 0: 
    division = n1/n2
    print(division)