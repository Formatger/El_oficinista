contraseña = "xert"

while True:
    respuesta  = input("Intrudce la contraseña: ")
    respuesta = respuesta.lower()
    if respuesta == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Vuelve a introducir el dato")