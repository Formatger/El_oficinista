frase = input("introduce frase: ")
letra = input("introduce letra: ")
contador = 0
frase = frase.lower()
letra = letra.lower()
for i in range(len(frase)):
    if frase[i] == letra:
        contador = contador + 1
print(contador)
