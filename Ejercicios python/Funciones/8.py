import numpy as np

lista = input("Introduce numeros separados por coma: ")
lista2 = lista.split(",")
lista2_enteros = [float(cadena) for cadena in lista2]
lista3 = []
datos = {'media':None , 'varianza': None , 'desviación típica': None}
print(datos)


def media():
    sumatorio=0
    for valor in lista2_enteros:
        sumatorio += valor
    
    media = sumatorio /(len(lista2_enteros))

    return media

def varianza():
    varianza = np.var(lista2_enteros)

    return varianza

def d_tipica():
    d_tip = np.std(lista2_enteros)

    return d_tip




datos['media'] = media()
datos['varianza'] = varianza()
datos['desviación típica'] = d_tipica()
print(datos)