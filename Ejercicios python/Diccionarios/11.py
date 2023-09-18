cliente  = {}
info = {}

data = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

lista1 = data.split("\n")
lista2 = lista1[0].split(";")
lista2.pop(0)
lista1.pop(0)

for valor in lista1:
    lista3 = valor.split(";")
    a = lista3.pop(0)
    i=0
    for valor in lista3:
        info[lista2[i]] = valor
        i +=1
        cliente[a]=info

print(cliente)
