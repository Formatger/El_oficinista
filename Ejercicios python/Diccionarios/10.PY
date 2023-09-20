import sqlite3

data = sqlite3.connect(
    "/Users/albertformatger/Desktop/El_oficinista-1/Ejercicios python/Diccionarios/Datos_clientes.db"
)
cursor = data.cursor()
consulta = "SELECT name FROM sqlite_master WHERE type='table' AND name='Clientes'"
tabla_existe = cursor.fetchone()
cursor.execute(consulta)

if not tabla_existe:
    tabla = """CREATE TABLE IF NOT EXISTS Clientes (
               NIF TEXT PRIMARY KEY, 
               nombre TEXT, 
               direccion TEXT, 
               telefono TEXT, 
               correo TEXT, 
               preferente BOOLEAN)"""
    cursor.execute(tabla)

cliente = {}
info = {}

while True:
    decision = input(
        "Que desea? (Añadir cliente, Eliminar cliente, Mostrar cliente, Listar clientes, Listar preferentes, Terminar): "
    )

    if decision.lower() == "añadir cliente":
        info = {}
        introduce = input(
            "Introduce la información separada por ',' (NIF, nombre, dirección, teléfono, correo, preferente(True si es cliente preferente)): "
        )
        info2 = introduce.split(",")
        i = 1
        descrip = ("NIF", "nombre", "dirección", "teléfono", "correo", "preferente")
        for valor in range(1, len(info2)):
            info[descrip[i]] = info2[valor]
            i += 1
        cliente[info2[0]] = info

        # Insertar los datos en la base de datos
        cursor.execute(
            "INSERT INTO Clientes (NIF, nombre, direccion, telefono, correo, preferente) VALUES (?, ?, ?, ?, ?, ?)",
            (
                info2[0],
                info["nombre"],
                info["dirección"],
                info["teléfono"],
                info["correo"],
                info["preferente"],
            ),
        )
        data.commit()  # Guardar los cambios en la base de datos

    if decision.lower() == "eliminar cliente":
        nif = input("Introduce el NIF del cliente")
        # cliente.pop(nif)

        # Eliminar el registro de la base de datos
        cursor.execute("DELETE FROM Clientes WHERE NIF=?", (nif,))
        data.commit()  # Guardar los cambios en la base de datos

    if decision.lower() == "mostrar cliente":
        nif = input("Introduce el NIF del cliente")
        # Ejecutar una consulta SQL para seleccionar el cliente con el NIF especificado
        cursor.execute("SELECT * FROM Clientes WHERE NIF=?", (nif,))
        cliente_encontrado = cursor.fetchone()
        print(cliente_encontrado)

    if decision.lower() == "listar clientes":
        cursor.execute("SELECT * FROM Clientes")
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
        # for valor, result in cliente.items():
        #      print(f"{valor}___{result['nombre']}")

    if decision.lower() == "listar preferentes":
        cursor.execute("SELECT * FROM Clientes")
        registros = cursor.fetchall()
        for registro in registros:
            if registro[5] == "True":
                print(registro)

        # preferente = []
        # for valor, data in cliente.items():
        #     if data['preferente'] == "True":
        #         preferente.append(data['nombre'])
        # print(preferente)

    if decision.lower() == "terminar":
        data.commit()
        break

data.commit()
data.close()
print("Vuelve a iniciar el programa para editar la base de datos")
