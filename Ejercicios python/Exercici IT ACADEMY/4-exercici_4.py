import sqlite3

conexion = sqlite3.connect("C:\\Users\\Merche\\Desktop\\El Oficinista\\Ejercicios python\\Exercici IT ACADEMY\\data.db")
cursor = conexion.cursor()

cursor.execute('''SELECT p.person_name, COUNT(DISTINCT mp.role_id) AS repeticiones 
               FROM tb_movie_person mp JOIN tb_person p 
               ON p.person_id = mp.person_id 
               GROUP BY p.person_id''')
info3 = cursor.fetchall()
print(info3)


cursor.execute('''
               SELECT p.person_name, COUNT(DISTINCT mp.role_id) AS repeticiones 
               FROM tb_movie_person mp JOIN tb_person p 
               ON p.person_id = mp.person_id 
               GROUP BY p.person_id
               HAVING repeticiones >1''')
info3 = cursor.fetchall()
print(info3)