correo = input("introduce email:")
indice = correo.index("@")
print(correo.find("@"))
prefijo = correo[:indice]
print(f"{prefijo}@.ceu.es")

#correo.find() devuelve la posicion en que s eencuentra el caracter buscado