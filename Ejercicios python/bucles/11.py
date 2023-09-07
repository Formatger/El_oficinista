palabra = input("introduce una palabra: ")
palabra_reves = str()
for i in range(len(palabra), -1, -1):
    palabra_reves = palabra[i]
    print(palabra_reves)