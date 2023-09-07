nombres = input("Introduc el nombre completo")
nombre_sinespacio = ""
for valor in nombres:
    if valor != " ":      
        nombre_sinespacio = nombre_sinespacio + valor
print(f"{nombres.upper()} tiene {len(nombre_sinespacio)} letras")