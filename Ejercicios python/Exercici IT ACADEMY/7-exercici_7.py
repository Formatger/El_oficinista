import sqlite3

conexion = sqlite3.connect(
    "/Users/albertformatger/Desktop/El_oficinista-1/Ejercicios python/Exercici IT ACADEMY/data.db"
)
cursor = conexion.cursor()

cursor.execute(
    """UPDATE tb_movie 
               SET movie_genre_id = 3
               WHERE movie_title = 'Ocho Apellidos Catalanes' """
)

conexion.commit()
conexion.close()
