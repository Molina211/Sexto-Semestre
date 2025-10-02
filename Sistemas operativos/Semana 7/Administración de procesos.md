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

### Estados de procesos

- **Ejecución**: El proceso está corriendo en la CPU.

- **Bloqueado**: El proceso espera un recurso externo (E/S, archivo, etc.).

- **Listo**: Está preparado para ejecutarse, esperando turno en la CPU.

- **En espera**: Similar a bloqueado, pero esperando que se cumpla una condición.

- **Suspendido**: El proceso está detenido temporalmente, puede reanudarse más tarde.

### Bloque de control de procesos (PCB – Process Control Block)

Es una estructura en memoria que almacena toda la información necesaria para gestionar un proceso. Incluye:

- **Identificador de un proceso (PID)**: Número único que distingue a cada proceso.

- **Nombre de un proceso**: Etiqueta o denominación asignada al proceso.

- **Estado del proceso**: Indica si está en ejecución, listo, bloqueado, etc.

- **Localizar memoria del proceso**: Direcciones de memoria donde está el código, datos y pila.

- **Proceso procesando por prioridad**: Nivel de importancia que determina el orden de ejecución frente a otros procesos.

| **Contenido del PCB**             | **Descripción**                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Información de identificación** | ID del proceso, ID del proceso padre (si aplica) e información del usuario.                                         |
| **Estado del procesador**         | Valores del procesador al inicio del proceso o cuando es interrumpido.                                              |
| **Control del proceso**           | Estado y planificación, memoria asignada, recursos usados, punteros de colas/anillos y comunicación entre procesos. |

---

### Planificación de procesos

La planificación es el mecanismo mediante el cual el sistema operativo decide qué proceso ejecutar, cuánto tiempo y cuándo asignarle recursos. Es fundamental para el buen funcionamiento del S.O., pues busca:

- Reparto equitativo y uso eficiente del procesador.

- Reducir tiempos de respuesta y de espera.

- Aumentar la cantidad de trabajos ejecutados por unidad de tiempo.

La selección se realiza mediante algoritmos de planificación, que definen las políticas para pasar procesos de listo a ejecución. Esta tarea la realiza el planificador, que gestiona los procesos listos en diferentes niveles de planificación.

El sistema operativo organiza la ejecución de los procesos.

- **A largo plazo**: Decide qué procesos entran al sistema (control de admisión de trabajos).

- **A mediano plazo**: Suspende o reanuda procesos para equilibrar la carga y optimizar recursos.

- **A corto plazo**: Selecciona qué proceso en la cola lista usa la CPU en ese momento.

---

### Algoritmos de planificación

Métodos que determinan el orden de ejecución de los procesos en la CPU.

- **Round Robin (RR)**: Cada proceso recibe un “quantum” (tiempo fijo). Si no termina, pasa al final de la cola.

- **FIFO (First In, First Out)**: El primero que llega es el primero en ejecutarse (cola simple).

- **SJF (Shortest Job First)**: Se ejecuta primero el proceso con la duración más corta.

- **SRTF (Shortest Remaining Time First)**: Variante de SJF, siempre se ejecuta el proceso con menos tiempo restante; puede interrumpir a otros.

- **Aleatorio**: Selección de procesos de forma no determinista, útil solo en casos especiales.

- **Tiempo real**: Procesos críticos que deben ejecutarse en un tiempo exacto o antes de un límite.

- **Prioridades**: Los procesos con mayor prioridad se ejecutan antes que los de menor prioridad.

| **Algoritmo**                    | **Descripción**                                                                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Round-robin o cíclica**        | Reparte equitativamente el tiempo del procesador (sistemas de tiempo compartido). Los procesos se ejecutan en orden circular hasta que terminan su rodaja o se bloquean. |
| **FIFO**                         | Los procesos se ejecutan en el orden en que llegaron (primero en entrar, primero en salir).                                                                              |
| **Prioridades**                  | Se ejecuta primero el proceso con mayor prioridad. Puede ocurrir inanición si procesos de baja prioridad nunca se ejecutan. Se soluciona con envejecimiento.             |
| **Primero el trabajo más corto** | Se ejecuta el proceso con menor tiempo de ejecución conocido. Puede haber inanición.                                                                                     |
| **Aleatorio o lotería**          | Se elige al azar el proceso a ejecutar (usando números aleatorios).                                                                                                      |
| **Tiempo real**                  | Procesos que deben ejecutarse en un instante específico o repetitivamente en intervalos fijos.                                                                           |

---

### Señales, excepciones y temporizadores

**Señales y Excepciones en SO**

- Los sistemas operativos notifican eventos a los procesos mediante:
  
  - **Señales** → usadas en sistemas POSIX.
  
  - **Excepciones** → usadas en Windows NT.

- Ambos mecanismos cumplen la misma función frente a un proceso.

- Los procesos también pueden recibir notificaciones programadas mediante temporizadores.

**Señales**

- Son interrupciones a un proceso, generadas por el SO u otro proceso.

- Tipos:
  
  1. Excepciones de hardware.
  
  2. Comunicación.
  
  3. Entrada/Salida asíncrona.
  
  4. Activadas por otro proceso.

- **Efectos sobre el proceso:**
  
  1. Se detiene en la instrucción actual.
  
  2. Ejecuta una rutina de tratamiento (parte del mismo proceso).
  
  3. Retoma la ejecución donde fue interrumpido.

**Restricciones**

- Un proceso puede enviar señales a otros solo si pertenecen al mismo usuario.

- El superusuario puede enviar señales a procesos de cualquier usuario.

---

**Procesos ligeros o hilos**

Los hilos (threads) son flujos de ejecución dentro de un mismo proceso. El primero es el hilo principal, asociado a la función `main()` en C++.

**Qué comparten los hilos de un proceso**:

- Espacio de memoria

- Variables globales

- Archivos abiertos

- Procesos hijos

- Temporizadores

- Señales, semáforos y contabilidad

**Qué no comparten (propio de cada hilo)**:

- Contador de programa

- Pila

- Registros

- Estado del hilo

**Ventajas del uso de hilos**:

- Separación y organización de tareas.

- Modularidad en trabajos complejos.

- Mayor velocidad al aprovechar tiempos de espera.

- Uso más eficiente del procesador.

- Permite funciones adicionales, como revisión ortográfica en segundo plano en Word.

- 

---

**Servicios POSIX**

- **POSIX (Portable Operating System Interface)** es un estándar que define cómo debe comportarse un sistema operativo tipo Unix.

- Incluye servicios para:
  
  - **Manejo de procesos e hilos**
  
  - **Comunicación entre procesos (IPC)**
  
  - **Señales**
  
  - **Temporizadores**
  
  - **Archivos y directorios**
