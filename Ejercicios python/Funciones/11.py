frase = input("escribe una frase: ")
list_frase = frase.split(" ")
dic = {}

def diccionario():
    for valor in list_frase:
        dic[valor] = list_frase.count(valor)
    
    return dic

a = diccionario()

def valormax():
    max=0
    for key in dic:
        if dic[key] > max:
            max = dic[key]
            tupla = (key,max)
    return tupla

b = valormax()



print(a)

print(b)





