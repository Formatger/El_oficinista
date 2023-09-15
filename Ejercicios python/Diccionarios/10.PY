cliente = {}
info = {}

while True:
    decision = input("Que desea? (Añadir cliente, Eliminar cliente, Mostrar cliente, Listar clientes, Listar preferentes, Terminar): ")
   
    if decision.lower() == "añadir cliente":
        info = {}
        introduce = input("Introduce la información separada por ',' (NIF, nombre, dirección, teléfono, correo, preferente(True si es cliente preferente)): ")
        info2 = introduce.split(',')
        i=1
        descrip = ('NIF','nombre','dirección','teléfono','correo','preferente')
        for valor in range(1, len(info2)):
            info[descrip[i]] = info2[valor]
            i +=1
        cliente[info2[0]] = info

    if decision.lower() == "eliminar cliente":
        nif = input("Introduce el NIF del cliente")
        cliente.pop(nif)

    if decision.lower() == "mostrar cliente":
        nif = input("Introduce el NIF del cliente")
        print(cliente[nif])

    if decision.lower() == "listar clientes":
        for valor, result in cliente.items():
            print(f"{valor}___{result['nombre']}")
    
    if decision.lower() == "listar preferentes":
        preferente = []
        for valor, data in cliente.items():
            if data['preferente'] == "True":
                preferente.append(data['nombre'])
        print(preferente)

    if decision.lower() == "terminar":
        break

print("Vuelve a iniciar el programa para editar la base de datos")