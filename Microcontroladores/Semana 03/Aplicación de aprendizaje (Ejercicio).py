#Desarrollar una interfaz de usuario usando Tkinter para una calculadora de porcentaje de grasa corporal.

import tkinter as tk
from PIL import Image, ImageTk

def grasa_corporal_general(peso, altura, edad, sexo):

    imc = peso / (altura ** 2)
    
    if sexo.lower() == "hombre":
        return 1.20 * imc + 0.23 * edad - 16.2
    elif sexo.lower() == "mujer":
        return 1.20 * imc + 0.23 * edad - 5.4
    else:
        raise ValueError("Sexo inválido. Use 'hombre' o 'mujer'.")
def calcular():
    try:
        peso = float(peso_entry.get())
        altura = float(altura_entry.get())
        edad = int(edad_entry.get())
        sexo = sexo_entry.get().strip().lower()
        resultadoFinal = grasa_corporal_general(peso, altura, edad, sexo)
        resultadoFinal_label.config(text=f"Porcentaje de grasa corporal: {resultadoFinal:.2f}%")
    except ValueError as e:
        resultadoFinal_label.config(text=f"Error: {e}")
        
root = tk.Tk()
root.title("Calculadora de porcentaje de grasa corporal")
root.geometry("320x480")

imagen = Image.open('C:\Pregrado Ingenieria en Sistemas\Semestre 6\Microcontroladores\Semana 3\porcentaje-grasa-corporal.jpg.jpg')
imagen = imagen.resize((300, 200), Image.Resampling.LANCZOS)
Imagen_tk = ImageTk.PhotoImage(imagen)
label = tk.Label(root, image=Imagen_tk)
label.pack(side="top", fill="x")

tk.Label(root, text="Ingrese su peso (kg)").pack()
peso_entry = tk.Entry(root)
peso_entry.pack(fill="x", padx=10)

tk.Label(root, text="Ingrese su altura").pack()
altura_entry = tk.Entry(root)
altura_entry.pack(fill="x", padx=10)

tk.Label(root, text="Ingrese su edad").pack()
edad_entry = tk.Entry(root)
edad_entry.pack(fill="x", padx=10)

tk.Label(root, text="Ingrese su sexo (hombre/mujer)").pack()
sexo_entry = tk.Entry(root)
sexo_entry.pack(fill="x", padx=10)

tk.Button(root, text="Calcular", command=calcular).pack(pady=10)

resultadoFinal_label = tk.Label(root, text="")
resultadoFinal_label.pack(pady=10)
root.mainloop()