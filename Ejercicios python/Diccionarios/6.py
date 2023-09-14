p = {}
x={}
b = ['Nombre', 'edad', 'sexo', 'teléfono', 'correo electronico']
i = 0
a = []
while True:
    info = input("Nombre, edad, sexo, teléfono, correo electronico (separado pro comas): ")
    if info == "salir":
        break
    a = info.split(",")
    for valor in a:
        p[b[i]] = a[i]
        i +=1
        if i > len(a):
            p = p.update(p)
    i=0
    print(p)

print(x)

