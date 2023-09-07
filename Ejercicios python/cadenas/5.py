frase = input("pon una frase")
frase_invertida = ""
for valor in frase:
    frase_invertida = valor + frase_invertida

print(frase_invertida)
print(frase[::-1])