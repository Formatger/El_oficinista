import sqlite3

conexion = sqlite3.connect(
    "/Users/albertformatger/Desktop/El_oficinista-1/Ejercicios python/Exercici IT ACADEMY/data.db"
)
cursor = conexion.cursor()

cursor.execute(
    """SELECT person_name, person_country, person_dob 
               FROM tb_person 
               WHERE person_dod IS NULL 
               ORDER BY person_dob"""
)

resultado = cursor.fetchall()
print(resultado)

# cursor.execute("SELECT * FROM tb_person WHERE person_dod IS NULL")
# resultado = cursor.fetchall()

# lista2=[]
# for result in resultado:
#     # print(result[1],result[2],result[3])
#     lista =[result[1],result[2],result[3]]
#     lista2.append(lista)

# lista2_ordenada = sorted(lista2, key=lambda x: x[2])

# for valor in lista2_ordenada:
#     print(valor[0],valor[1],valor[2])
