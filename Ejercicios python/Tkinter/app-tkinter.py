import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Hola desde tu aplicación!")


ventana = tk.Tk()
ventana.title("MI APLICACION")

boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)

boton.pack(pady=20)

ventana.mainloop()