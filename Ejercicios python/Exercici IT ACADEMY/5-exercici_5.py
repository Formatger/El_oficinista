import sqlite3

conexion = sqlite3.connect("C:\\Users\\Merche\\Desktop\\El Oficinista\\Ejercicios python\\Exercici IT ACADEMY\\data.db")
cursor = conexion.cursor()

if not cursor.execute('''SELECT genre_name FROM tb_genre WHERE genre_name = 'Documental' '''):                     
    insertar = cursor.execute('''INSERT INTO tb_genre (genre_id, genre_name)
    VALUES (69, 'Documental');''')
    conexion.commit()

cursor.execute('''SELECT genre_name 
               FROM tb_genre''')
print(cursor.fetchall())