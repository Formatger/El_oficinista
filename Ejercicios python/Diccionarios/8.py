trad = {}

info = input("introduce palabra y traducción( separa por : puntos y cada palabra nueva con ,): ")
a = info.split(",")
for valor in a:
    esp, ing = valor.split(":")
    trad[esp] = ing

frase = input("Introduce una frase: ")
palabras = frase.split()
traduccion = ""
for palabra in palabras:
    if palabra in trad:
        traduccion += f" {trad[palabra]}"
    else:
        traduccion += f" {palabra}"
print(trad)
print(traduccion)






