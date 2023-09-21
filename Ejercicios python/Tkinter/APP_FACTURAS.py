import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


#CREACION BASE DE DATOS Y TABLA
import sqlite3
conexion = sqlite3.connect("C:\\Users\\Merche\\Desktop\\El Oficinista\\Ejercicios python\\Tkinter\\data_facturas.db")
cursor = conexion.cursor()
cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='data' ''')
tabla_existe = cursor.fetchall()

if not tabla_existe:
    tabla = '''CREATE TABLE IF NOT EXISTS data (
             factura TEXT PRIMARY KEY,
             precio FLOAT)'''
    cursor.execute(tabla) 
    conexion.commit()

facturas = {}

#DEFINIR LAS DOS ACCIONES POSIBLES COMO FUNCIONES

def agregar_factura():
    num_factura = entrada_num_factura.get()
    precio_factura = entrada_valor_factura.get()
    precio_factura = precio_factura.replace(',','.')
    precio_factura = float(precio_factura)
    cursor.execute('''INSERT INTO data (factura, precio)
                   VALUES (?,?)''', (num_factura, precio_factura))
    conexion.commit()
    entrada_num_factura.delete(0,tk.END)
    entrada_valor_factura.delete(0,tk.END)
    

def liquidar_factura():
    num_factura = entrada_num_factura_liquidar.get()
    comprobacion = cursor.execute('''SELECT * FROM data WHERE factura = ?''',(num_factura,))
    cursor.fetchone()
    if comprobacion:
        cursor.execute('''DELETE FROM data WHERE factura = (?) ''', (num_factura,))
    conexion.commit()
    entrada_num_factura_liquidar.delete(0, tk.END)

def mostrar_facturas_pendientes():
    for item in treeview.get_children():
        treeview.delete(item)
    cursor.execute('''SELECT * FROM data''')
    lista = cursor.fetchall()
    for factura in lista:
        treeview.insert("","end", values = factura)
        treeview.pack()



#INCIAR VENTA TKINTER

app = tk.Tk()
app.title("Gestión de Facturas")

frame_mostrar = tk.Frame(app)
frame_mostrar.pack()

treeview = ttk.Treeview(frame_mostrar, columns=("ID Factura", "Precio (€)"))
treeview.heading("ID Factura", text = "ID Factura")
treeview.heading("Precio (€)", text = "Precio (€)")
boton_mostrar = tk.Button(app, text="Mostrar Facturas Pendientes", command=mostrar_facturas_pendientes)
boton_mostrar.pack()



frame_añadir = tk.Frame(app)
frame_añadir.pack()

label_num_factura = tk.Label(frame_añadir, text="Número de Factura:")
label_valor_factura = tk.Label(frame_añadir, text="Valor:")

entrada_num_factura = tk.Entry(frame_añadir)
entrada_valor_factura = tk.Entry(frame_añadir)

boton_añadir = tk.Button(frame_añadir, text="Añadir Factura", command=agregar_factura)

label_num_factura.grid(row=0, column=0)
label_valor_factura.grid(row=1, column=0)
entrada_num_factura.grid(row=0, column=1)
entrada_valor_factura.grid(row=1, column=1)
boton_añadir.grid(row=2, columnspan=2)

frame_liquidar = tk.Frame(app)
frame_liquidar.pack()

label_num_factura_liquidar = tk.Label(frame_liquidar, text="Número de Factura a Liquidar:")
entrada_num_factura_liquidar = tk.Entry(frame_liquidar)
boton_liquidar = tk.Button(frame_liquidar, text="Liquidar Factura", command=liquidar_factura)

label_num_factura_liquidar.grid(row=0, column=0)
entrada_num_factura_liquidar.grid(row=0, column=1)
boton_liquidar.grid(row=1, columnspan=2)

app.mainloop()

conexion.commit()
conexion.close()


# def bucle():
#     while True:
#         seguir = input("Que quieres hacer? (AÑADIR, LIQUIDAR, TERMINAR): ")
#         if seguir == "AÑADIR":
#             fact = input("Añade el número de factura y su valor, separado por ':':   ")
#             fact2 = fact.split(':')
#             facturas[fact2[0]] = fact2[1]
#         if seguir == "LIQUIDAR":
#             num = input("Escribe el numero de factura: ")
#             facturas.pop(num)
#         if seguir == "TERMINAR":
#             break

    # print(f"Nº de factura: {factura} - {precio}€ \n")