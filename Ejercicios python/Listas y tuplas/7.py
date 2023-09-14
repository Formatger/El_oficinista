import string

lista = list(string.ascii_lowercase)
print(lista)
lista_corregida = []
for i in lista:
    if (lista.index(i)+1) % 3 != 0:
        lista_corregida.append(i)

print(lista_corregida)
