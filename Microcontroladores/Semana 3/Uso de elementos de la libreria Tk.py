import tkinter as tk

root = tk.Tk()
root.title("Mi primera app")
root.geometry("320x200")
root.title("Widgets básicos")
tk.Label(root, text="Texto del label").pack()
nombre = tk.Entry(root)
nombre.pack(fill="x", padx=10)
salida = tk.Label(root, text="aun sin saludo")
salida.pack(pady=30)
def saludar():
    salida.config(text=f"Hola, {nombre.get()}!")

boton = tk.Button(root, text="Saludar", command=saludar).pack()
root.mainloop()

'''Las opciones para ubicar elementos en la ventana son grid, pack, place. 
Pack es rapido y lineal, Grid es manejo con tablas y repsonsive, y Place son posiciones absolutas '''


root = tk.Tk()
root.title("Mi primera app")
root.geometry("320x200")
root.title("Widgets básicos")
boton1 = tk.Button(root, text="Boton 1")
boton1.grid(row=0, column=0, sticky="e", padx=5, pady=5)
boton2 = tk.Button(root, text="Boton 2")
boton2.grid(row=0, column=1, sticky="e", padx=20, pady=20)
boton3 = tk.Button(root, text="Boton 3")
boton3.grid(row=0, column=2, sticky="e", padx=5, pady=5)
boton4 = tk.Button(root, text="Boron 4")
boton4.place(x=100, y=100, width=80, height=40)
root.mainloop()