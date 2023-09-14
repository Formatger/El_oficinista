palabra = input("introduce una palabra: ")

palabra2 = palabra[::-1]
print(palabra2)
if palabra==palabra2:
    print("es palindromo")
else:
    print("no es palindromo")

#Se puede pasar a lista la palabra, y luego hacer un lista.reverse() y comparar las listas