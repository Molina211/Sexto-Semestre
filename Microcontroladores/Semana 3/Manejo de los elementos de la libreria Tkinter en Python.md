# Manejo de los elementos de la libreria Tkinter en Python

---

##### ¿Qué es?

Tkinter es el módulo estándar (libreria) de Python para crear interfaces gráficas de usuario (GUI). Sirve para hacer ventanas, botones, cuadros de texto y otros elementos visuales en aplicaciones de escritorio.

---

##### ¿Para qué sirve?

Con él puedes:

- Crear ventanas.

- Agregar botones, etiquetas, menús, cuadros de texto, listas, etc.

- Hacer que tu programa sea interactivo y visual, en lugar de funcionar solo en consola.

---

#### Palabras reservadas

###### 1. **`pack()`**

- **Cómo funciona:** coloca los elementos uno tras otro, de manera lineal (vertical u horizontal), según el orden en que se van añadiendo.

- **Ventajas:**
  
  - Muy simple de usar.
  
  - Ideal cuando la interfaz es pequeña y no necesita mucho control de posición.

- **Limitaciones:**
  
  - Poco flexible.
  
  - Difícil de alinear varios elementos de forma compleja.

Se usa mucho para estructuras rápidas o sencillas.

```python
label.pack(side="top") button.pack(side="bottom")
```

---

###### 2. **`grid()`**

- **Cómo funciona:** organiza los elementos en una rejilla de filas y columnas (como una tabla).

- **Ventajas:**
  
  - Da un control ordenado y estructurado.
  
  - Permite hacer interfaces responsivas, ya que se pueden expandir o contraer filas/columnas.

- **Limitaciones:**
  
  - No se puede usar al mismo tiempo con pack() en la misma ventana/contenedor.

Se usa para formularios, paneles y diseños más complejos.

```python
label.grid(row=0, column=0) 
entry.grid(row=0, column=1) 
button.grid(row=1, column=0, columnspan=2)
```

---

###### 3. **`place()`**

- **Cómo funciona:** ubica los elementos en posiciones absolutas (x, y) o relativas al tamaño del contenedor.

- **Ventajas:**
  
  - Máximo control sobre la posición exacta de cada widget.
  
  - Útil cuando quieres que algo esté en un punto específico.

- **Limitaciones:**
  
  - No es responsivo (si la ventana cambia de tamaño, los elementos pueden quedar mal ubicados).

Se usa cuando necesitas control pixel-perfect, como en juegos o diseños fijos.

```python
button.place(x=50, y=100)
```

---

**EJemplos práctivos**

##### Ejemplos 1:

```python
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
```

**Visualización**

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-19-06-57-11-image.png)



##### Ejemplo 2:

```python
import tkinter as tk

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
```

**Visualización**

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-19-07-00-48-image.png)

---

#### Ejercicio

Desarrollar una interfaz de usuario usando Tkinter para una calculadora de porcentaje de grasa corporal.



```python
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
```

**Visualización**

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-19-07-52-19-image.png)
