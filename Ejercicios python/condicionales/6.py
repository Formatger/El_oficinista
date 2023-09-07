nombre = input("escribe tu nombre: ")
sexo = input("Masculino o femenino: ")
sexo = sexo.lower()
nombre = nombre.lower()
if sexo == "masculino" and nombre[0] > "n":
    print("Grupo A")
elif sexo == "femenino" and nombre[0] < "m":
    print("Grupo A")
else:
    print("Grupo B")