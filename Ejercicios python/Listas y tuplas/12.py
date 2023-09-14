import numpy as np

a = np.array([[1,2,3],
     [4,5,6]])
b = np.array([[-1,0],
     [0,1],
     [1,1]])

c = np.dot(a, b)
print(c)
print(len(a))


# a = ((1, 2, 3),
#      (4, 5, 6))
# b = ((-1, 0),
#      (0, 1),
#      (1,1))
# result = [[0,0],
#           [0,0]]
# for i in range(len(a)):
#     for j in range(len(b[0])):
#         for k in range(len(b)):
#             result[i][j] += a[i][k] * b[k][j]
# for i in range(len(result)):
#     result[i] = tuple(result[i])
# result = tuple(result)
# for i in range(len(result)):
#     print(result[i])


# # EXPLICACION CÓDIGO********************  Inicializamos la matriz de resultado con ceros.
# result = [[0, 0],
#           [0, 0]]
# Definimos dos matrices a y b, que son matrices 2x3 y 3x2, respectivamente. Luego, creamos una matriz vacía result que tendrá el mismo número de filas que a y el mismo número de columnas que b.
# python
# Copy code
# # Realizamos la multiplicación de matrices manualmente.
# for i in range(len(a)):
#     for j in range(len(b[0])):
#         for k in range(len(b)):
#             result[i][j] += a[i][k] * b[k][j]
# Utilizamos tres bucles for anidados para calcular cada elemento de la matriz resultante result. Los bucles exteriores iteran sobre las filas de a (variable i) y las columnas de b (variable j). El bucle interno (variable k) se utiliza para multiplicar los elementos correspondientes de las matrices a y b, y el resultado se suma al elemento correspondiente de la matriz result.
# python
# Copy code
# # Convertimos la matriz de resultado a tuplas.
# for i in range(len(result)):
#     result[i] = tuple(result[i])
# Después de calcular todos los elementos de la matriz resultante result, convertimos cada fila de la matriz result en una tupla, de modo que obtengamos una lista de tuplas en lugar de una lista de listas.
# python
# Copy code
# # Convertimos la matriz de resultado final a una tupla de tuplas.
# result = tuple(result)

# # Imprimimos el resultado.
# for i in range(len(result)):
#     print(result[i])
# Finalmente, convertimos la matriz result completa en una tupla de tuplas y luego imprimimos cada fila de la matriz resultante en un bucle for.
# La salida del código es:

# scss
# Copy code
# (2, 5)
# (2, 11)
# Estos son los resultados correctos de la multiplicación de matrices a y b. Cada elemento en la matriz resultante se calcula adecuadamente.





