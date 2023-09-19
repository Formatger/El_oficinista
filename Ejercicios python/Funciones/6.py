muestra = input("Lista numeros separados por coma: ")
lista = muestra.split(",")
lista2 = []

for valor in lista:
    lista2.append(float(valor))

def media():
    sumatorio=0
    for valor in lista2:
        sumatorio += valor
    
    media = sumatorio /(len(lista2))

    return media


resultado = media()
print(resultado)

