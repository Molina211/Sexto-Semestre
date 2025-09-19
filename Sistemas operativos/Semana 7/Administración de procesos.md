# Administración de procesos

---

## Concepto de proceso

Un proceso es un programa en ejecución que incluye el código, datos, recursos asignados y su estado dentro del sistema operativo.

**Jerarquía de los procesos**

- **Abuelo**: Proceso inicial que origina a otros procesos padres.

- **Padre**: Proceso que crea (engendra) a otro proceso.

- **Hijo**: Proceso creado por otro (hereda recursos del padre).

- **Hermano**: Procesos que comparten el mismo padre.

**Tipos de procesos**

- **Monotarea o monoproceso**: Solo se ejecuta un proceso a la vez.

- **Multitarea o multiproceso**: Se ejecutan varios procesos de forma concurrente.

- **Monousuario**: El sistema solo admite un usuario a la vez.

- **Multitramo**: El sistema divide la CPU en "tramos" de tiempo para asignarlos a procesos.

- **Tiempo real**: Procesos que deben responder en un tiempo estricto (ej. control de robots, aviones).

## Estados de procesos

- **Ejecución**: El proceso está corriendo en la CPU.

- **Bloqueado**: El proceso espera un recurso externo (E/S, archivo, etc.).

- **Listo**: Está preparado para ejecutarse, esperando turno en la CPU.

- **En espera**: Similar a bloqueado, pero esperando que se cumpla una condición.

- **Suspendido**: El proceso está detenido temporalmente, puede reanudarse más tarde.

**Bloque de control de procesos (PCB – Process Control Block)**

Es una estructura en memoria que almacena toda la información necesaria para gestionar un proceso. Incluye:

- **Identificador de un proceso (PID)**: Número único que distingue a cada proceso.

- **Nombre de un proceso**: Etiqueta o denominación asignada al proceso.

- **Estado del proceso**: Indica si está en ejecución, listo, bloqueado, etc.

- **Localizar memoria del proceso**: Direcciones de memoria donde está el código, datos y pila.

- **Proceso procesando por prioridad**: Nivel de importancia que determina el orden de ejecución frente a otros procesos.

---

**Planificación de procesos**

Es la forma en que el sistema operativo organiza la ejecución de los procesos.

- **A largo plazo**: Decide qué procesos entran al sistema (control de admisión de trabajos).

- **A mediano plazo**: Suspende o reanuda procesos para equilibrar la carga y optimizar recursos.

- **A corto plazo**: Selecciona qué proceso en la cola lista usa la CPU en ese momento.

---

**Algoritmos de planificación**

Métodos que determinan el orden de ejecución de los procesos en la CPU.

- **Round Robin (RR)**: Cada proceso recibe un “quantum” (tiempo fijo). Si no termina, pasa al final de la cola.

- **FIFO (First In, First Out)**: El primero que llega es el primero en ejecutarse (cola simple).

- **SJF (Shortest Job First)**: Se ejecuta primero el proceso con la duración más corta.

- **SRTF (Shortest Remaining Time First)**: Variante de SJF, siempre se ejecuta el proceso con menos tiempo restante; puede interrumpir a otros.

- **Aleatorio**: Selección de procesos de forma no determinista, útil solo en casos especiales.

- **Tiempo real**: Procesos críticos que deben ejecutarse en un tiempo exacto o antes de un límite.

- **Prioridades**: Los procesos con mayor prioridad se ejecutan antes que los de menor prioridad.

**Señales, excepciones y temporizadores**

- **Señales**: Mecanismos de comunicación entre procesos y el sistema (ej. terminar un proceso con `kill`).

- **Excepciones**: Eventos inesperados que interrumpen la ejecución (ej. división por cero).

- **Temporizadores**: Relojes del sistema que permiten medir tiempo o limitar cuánto puede usar la CPU un proceso.

---

**Procesos ligeros o hilos**

- También llamados threads.

- Son “subprocesos” dentro de un mismo proceso, que comparten recursos pero pueden ejecutarse en paralelo.

- Permiten mayor eficiencia en tareas concurrentes.

---

**Servicios POSIX**

- **POSIX (Portable Operating System Interface)** es un estándar que define cómo debe comportarse un sistema operativo tipo Unix.

- Incluye servicios para:
  
  - **Manejo de procesos e hilos**
  
  - **Comunicación entre procesos (IPC)**
  
  - **Señales**
  
  - **Temporizadores**
  
  - **Archivos y directorios**




