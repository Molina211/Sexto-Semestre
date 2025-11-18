## **Algoritmos de Reemplazo de Páginas**

| Algoritmo | Qué es                                                                                     | Para qué sirve                                                                  | Qué hace el código en sí                                                                                                                             |
| --------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FIFO**  | First-In, First-Out. Elimina la página que lleva más tiempo en memoria.                    | Gestionar la memoria cuando se llena, reemplazando la página más antigua.       | Usa una cola para almacenar páginas; si la memoria está llena, elimina la más antigua; imprime el estado de memoria tras cada acceso.                |
| **LRU**   | Least Recently Used. Reemplaza la página menos recientemente usada.                        | Minimizar fallos de página basándose en uso reciente.                           | Actualiza la lista de páginas; elimina la menos recientemente usada si llega una nueva página y la memoria está llena; imprime el estado de memoria. |
| **OPT**   | Optimal. Reemplaza la página que no se usará por más tiempo en el futuro.                  | Servir como referencia teórica para medir eficiencia.                           | Calcula cuál página se usará más tarde y la reemplaza; agrega la nueva si hay espacio; imprime memoria tras cada acceso.                             |
| **LFU**   | Least Frequently Used. Reemplaza la página menos usada.                                    | Mantener en memoria las páginas más solicitadas.                                | Lleva un contador de uso; elimina la menos frecuentemente usada si la memoria está llena; imprime estado de memoria.                                 |
| **Clock** | Segunda oportunidad. Cada página tiene un bit de uso; si bit=1 recibe segunda oportunidad. | Evitar reemplazar páginas usadas frecuentemente, simulando un “reloj circular”. | Marca bit de uso al acceder; si falta espacio, recorre circularmente y reemplaza la primera con bit=0; imprime memoria tras cada acceso.             |

---

## **Algoritmos de Planificación de Procesos y Disco**

|Algoritmo|Qué es|Para qué sirve|Qué hace el código en sí|
|---|---|---|---|
|**Round Robin (RR)**|Planificación de procesos por quantum fijo.|Garantizar reparto equitativo del CPU entre procesos.|Toma el primer proceso, lo ejecuta por quantum o tiempo restante; si no termina, lo devuelve al final de la cola; imprime ejecución de cada proceso; repite hasta terminar todos.|
|**FCFS**|First-Come, First-Served. Atiende solicitudes en orden de llegada.|Planificación simple de disco o CPU.|Mueve el cabezal a cada solicitud en orden de llegada; imprime cada movimiento; no optimiza desplazamientos.|
|**SSTF**|Shortest Seek Time First. Atiende la solicitud más cercana al cabezal.|Reducir el tiempo de búsqueda del disco.|Calcula la distancia a cada solicitud pendiente; mueve el cabezal a la más cercana; elimina la atendida; imprime movimientos.|
|**SCAN**|Elevator. El cabezal se mueve en una dirección hasta atender todas las solicitudes, luego invierte.|Reducir movimientos largos y dar servicio más justo.|Divide solicitudes en mayores y menores; atiende primero las mayores (subiendo), luego las menores (bajando); imprime movimientos.|
|**C-SCAN**|Circular SCAN. Igual que SCAN, pero al final “salta” al inicio.|Ofrecer tiempos de espera uniformes a todas las pistas.|Atiende las solicitudes mayores; salta al inicio; atiende las menores en orden ascendente; imprime movimientos del cabezal.|