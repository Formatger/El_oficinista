from collections import deque
#FIFO (first in first out)
fila = deque([1, 2])
fila.append(3) #añadir dato
fila.append(4)
fila.popleft() #borrar a izquierda

print(fila)


#LIFO ( Last in first out) por ejemplo un historial de navegación

pila= []
pila.append(1)
pila.append(6)
pila.append(45)
print(pila)

ultimoelemento = pila.pop()
print(ultimoelemento)
pila.pop()
pila.pop()

if not pila:
    print("vacio")

