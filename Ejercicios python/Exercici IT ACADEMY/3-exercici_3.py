import sqlite3

conexion = sqlite3.connect("C:\\Users\\Merche\\Desktop\\El Oficinista\\Ejercicios python\\Exercici IT ACADEMY\\data.db")
cursor = conexion.cursor()

cursor.execute('''SELECT genre_name, COUNT(movie_genre_id) 
               FROM tb_genre JOIN tb_movie 
               ON movie_genre_id = genre_id 
               GROUP BY genre_name 
               ORDER BY COUNT (movie_genre_id) DESC''')
info = cursor.fetchall()
print(info)

# cursor.execute("SELECT * FROM tb_movie")
# a = cursor.fetchall()
# lista = []
# for valor in a:
#     lista_lin = [valor[1], valor[4]]
#     lista.append(lista_lin)

# conteo_valores = {}

# for valor in lista:
#     a = valor[1]
#     if a in conteo_valores:
#         conteo_valores[a] +=1
#     else:
#         conteo_valores[a] = 1

# conteo_valores =  conteo_valores.items()
# conteo_valores = sorted(conteo_valores, key=lambda x:x[1], reverse=True)
# conteo_valores = dict(conteo_valores)

# cursor.execute("SELECT genre_id, genre_name FROM tb_genre")
# a = cursor.fetchall()
# a=dict(a)
# resultado={}

# for valor in conteo_valores:
#     palabra = a[valor]
#     resultado[palabra] = conteo_valores[valor]

# print(resultado)