import tkinter as tk

ventana = tk.Tk()

ventana.title("unitecnar APP",)

ventana.geometry("800x600")

ventana.resizable(True,True)

titulo =tk.Label(ventana, text="LOGIN", font=("Arial", 20), fg="blue")
titulo.pack()

nombre = tk.Label(ventana, text="NOMBRE").place(x=20, y=60)
txtNombre = tk.Entry(ventana).place(x=130, y=60)

nombre = tk.Label(ventana, text="NICKNAME").place(x=20, y=100)
txtNombre = tk.Entry(ventana).place(x=130, y=100)

nombre = tk.Label(ventana, text="CONTRASEÑA").place(x=20, y=130)

txtContrasena = tk.Entry(ventana, show="*")
txtContrasena.place(x=130, y=130)

boton= tk.Button(ventana, text="LOGIN")
boton.place(x=130, y=170)
ventana.mainloop()