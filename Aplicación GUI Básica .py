import tkinter as tk
from tkinter import messagebox

# Función para agregar un elemento a la lista
def agregar_elemento():
    dato = entry.get()
    if dato:
        lista.insert(tk.END, dato)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "insertar datos")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica uea")

# Crear una etiqueta
label = tk.Label(root, text="UEA")
label = tk.Label(root, text="TIC")
label = tk.Label(root, text="Ingrese un dato:")
label.pack(pady=10)

# Crear un campo de texto
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Crear un botón para agregar datos
agregar_btn = tk.Button(root, text="Agregar", command=agregar_elemento)
agregar_btn.pack(pady=5)

# Crear una lista para mostrar los datos
lista = tk.Listbox(root, width=50, height=10)
lista.pack(pady=10)

# Crear un botón para limpiar la lista
limpiar_btn = tk.Button(root, text="Limpiar", command=limpiar_lista)
limpiar_btn.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
