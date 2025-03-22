import tkinter as tk
from tkinter import messagebox

# Clase Usuarios para manejar la lista de usuarios
class Usuarios:
    def __init__(self):
        self.lista_usuarios = []

    def guardarUsuario(self, nombre, correo):
        # Aquí guardamos el usuario en la lista
        self.lista_usuarios.append({'Nombre': nombre, 'Correo': correo})

    def listarUsuarios(self):
        # Devolvemos la lista de usuarios agregados
        return self.lista_usuarios

# Crear instancia global de Usuarios
usuario = Usuarios()

# Función para guardar un usuario
def guardar_usuario():
    nombre = entry_nombre.get()
    correo = entry_correo.get()

    if not nombre or not correo:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
        return

    # Llamamos al método guardarUsuario de la instancia de Usuarios
    usuario.guardarUsuario(nombre, correo)
    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    messagebox.showinfo("Guardado", "Usuario guardado correctamente.")

# Función para listar los usuarios
def listar_usuarios():
    # Limpiar panel de lista antes de mostrar nuevos datos
    panel_usuarios.config(state=tk.NORMAL)  # Hacer editable el panel temporalmente
    panel_usuarios.delete(1.0, tk.END)  # Limpiar el contenido

    usuarios = usuario.listarUsuarios()

    if usuarios:
        for user in usuarios:
            panel_usuarios.insert(tk.END, f"Nombre: {user['Nombre']}, Correo: {user['Correo']}\n")
    else:
        panel_usuarios.insert(tk.END, "No hay usuarios registrados.")
    
    panel_usuarios.config(state=tk.DISABLED)  # Deshabilitar el panel después de mostrar los usuarios

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Usuarios")

# Crear el formulario
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Correo:").grid(row=1, column=0, padx=10, pady=10)
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=1, column=1, padx=10, pady=10)

# Botón para guardar usuario
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_usuario)
boton_guardar.grid(row=2, column=0, columnspan=2, pady=10)

# Botón para listar usuarios
boton_listar = tk.Button(ventana, text="Listar Usuarios", command=listar_usuarios)
boton_listar.grid(row=3, column=0, columnspan=2, pady=10)

# Panel para mostrar los usuarios
panel_usuarios = tk.Text(ventana, width=40, height=10, state=tk.DISABLED)
panel_usuarios.grid(row=4, column=0, columnspan=2, pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
