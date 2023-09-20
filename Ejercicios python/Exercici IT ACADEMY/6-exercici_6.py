import sqlite3

conexion = sqlite3.connect(
    "/Users/albertformatger/Desktop/El_oficinista-1/Ejercicios python/Exercici IT ACADEMY/data.db"
)
cursor = conexion.cursor()

cursor.execute(
    """DELETE FROM tb_movie
       WHERE movie_title = 'La Gran Familia Española'"""
)

conexion.commit()
conexion.close()
