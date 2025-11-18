# Narrativa/Conceptos

---

## **Algoritmos de Planificación de Procesos**

1. **Round Robin (RR)**
    
    - Simula la planificación de procesos usando **un quantum de tiempo fijo**.
        
    - Mantiene una **cola de procesos** listos para ejecutarse.
        
    - Toma el primer proceso de la cola y lo ejecuta por el tiempo **mínimo entre su tiempo restante y el quantum**.
        
    - Si el proceso no termina, se vuelve a agregar al final de la cola.
        
    - Repite el ciclo hasta que todos los procesos terminen.
        
    - Imprime la ejecución de cada proceso y cuánto tiempo se ejecutó en cada turno.
        
    - Al final, indica que **todos los procesos han terminado**.

## **Algoritmos de Reemplazo de Páginas**

1. **FIFO (First-In, First-Out)**
    
    - Simula el algoritmo FIFO de reemplazo de páginas.
        
    - Usa una cola para almacenar las páginas en memoria.
        
    - Cuando la memoria está llena y llega una nueva página, elimina la **página más antigua**.
        
    - Imprime el estado de la memoria después de cada acceso.
        
2. **LRU (Least Recently Used)**
    
    - Simula LRU usando una lista que se actualiza en cada acceso.
        
    - Si la página ya está en memoria, la mueve al final (más recientemente usada).
        
    - Si la memoria está llena y llega una página nueva, elimina la **menos recientemente usada**.
        
    - Imprime el estado de la memoria tras cada operación.
        
3. **OPT (Optimal)**
    
    - Simula el algoritmo óptimo de reemplazo de páginas.
        
    - Calcula cuál página no se usará **por más tiempo en el futuro** y la reemplaza.
        
    - Si hay espacio, agrega la nueva página directamente.
        
    - Imprime el estado de la memoria tras cada acceso.
        
4. **LFU (Least Frequently Used)**
    
    - Simula LFU usando un mapa de frecuencia.
        
    - Incrementa el contador de uso cada vez que una página es accedida.
        
    - Cuando la memoria está llena y llega una nueva página, elimina la **menos frecuentemente usada**.
        
    - Imprime el estado de la memoria después de cada acceso.
        
5. **Clock (Segunda oportunidad)**
    
    - Simula Clock con un arreglo de páginas y un arreglo de bits de uso.
        
    - Si la página está en memoria, marca su bit de uso como `true`.
        
    - Si la página no está, recorre circularmente hasta encontrar una página con bit `false` y la reemplaza.
        
    - Actualiza el puntero del “reloj” después de cada reemplazo.
        
    - Imprime el estado de la memoria tras cada operación.

## **Algoritmos de Planificación de Disco**

1. **FCFS (First-Come, First-Served)**
    
    - Simula la planificación de disco atendiendo solicitudes en **orden de llegada**.
        
    - Muestra cada movimiento del cabezal desde la posición actual a la solicitud siguiente.
        
    - Actualiza la posición del cabezal después de cada movimiento.
        
    - No optimiza movimientos, solo sigue el orden original.
        
2. **SSTF (Shortest Seek Time First)**
    
    - Simula SSTF seleccionando la solicitud **más cercana al cabezal** en cada paso.
        
    - Calcula la distancia del cabezal a todas las solicitudes pendientes.
        
    - Mueve el cabezal a la solicitud más cercana y la elimina de la lista.
        
    - Imprime cada movimiento del cabezal.
        
3. **SCAN (Elevator)**
    
    - Simula SCAN moviéndose primero en una dirección (subiendo) hasta atender todas las solicitudes mayores.
        
    - Luego invierte la dirección y atiende las solicitudes menores (bajando).
        
    - Divide las solicitudes en mayores y menores respecto a la posición inicial del cabezal.
        
    - Imprime cada movimiento del cabezal.
        
4. **C-SCAN (Circular SCAN)**
    
    - Simula C-SCAN moviéndose en una dirección hasta el final.
        
    - Cuando llega al final, “salta” al inicio y continúa en la misma dirección.
        
    - Divide las solicitudes en mayores y menores respecto a la posición inicial del cabezal.
        
    - Imprime cada movimiento, incluyendo el salto circular.