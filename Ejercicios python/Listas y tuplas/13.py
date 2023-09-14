a = input("Introduce numeros separados por coma: ")
a2 = a.split(',')
a3 = []
dividendo = 0

for num in a2:
    numero = int(num)
    a3.append(numero)

    
for i in a3:
    dividendo += i
media = dividendo / len(a2)
print(media)