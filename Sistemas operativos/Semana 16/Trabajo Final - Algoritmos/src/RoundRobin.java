import java.util.LinkedList;
import java.util.Queue;

// Clase principal que simula el algoritmo de planificación Round Robin
public class RoundRobin {

    // Clase interna que representa un proceso
    static class Proceso {
        String nombre;         // Nombre del proceso (por ejemplo, P1, P2...)
        int tiempoRestante;    // Tiempo que le queda por ejecutar al proceso

        // Constructor que inicializa el nombre del proceso y su tiempo de CPU
        Proceso(String nombre, int tiempoCPU) {
            this.nombre = nombre;
            this.tiempoRestante = tiempoCPU;
        }
    }

    public static void main(String[] args) {
        // Creamos una cola (ReemplazoDePagina.FIFO) para almacenar los procesos
        Queue<Proceso> cola = new LinkedList<>();

        // Añadimos tres procesos a la cola con sus respectivos tiempos de CPU
        cola.add(new Proceso("P1", 6));  // P1 necesita 6 ms
        cola.add(new Proceso("P2", 4));  // P2 necesita 4 ms
        cola.add(new Proceso("P3", 8));  // P3 necesita 8 ms

        int quantum = 3; // Quantum: tiempo máximo que un proceso puede ejecutarse antes de ceder CPU

        System.out.println("Simulación Round Robin:");

        // Bucle que se ejecuta mientras haya procesos en la cola
        while (!cola.isEmpty()) {
            // Sacamos el primer proceso de la cola (ReemplazoDePagina.FIFO)
            Proceso p = cola.poll();

            // Calculamos cuánto tiempo ejecutará este proceso:
            // Es el mínimo entre su tiempo restante y el quantum
            int tiempoEjecutado = Math.min(p.tiempoRestante, quantum);

            // Mostramos en consola qué proceso se está ejecutando y por cuánto tiempo
            System.out.println(p.nombre + " ejecuta " + tiempoEjecutado + " ms");

            // Reducimos el tiempo restante del proceso
            p.tiempoRestante -= tiempoEjecutado;

            // Si el proceso todavía tiene tiempo restante, se vuelve a agregar al final de la cola
            if (p.tiempoRestante > 0) {
                cola.add(p);
            }
        }

        // Mensaje final indicando que todos los procesos han terminado
        System.out.println("Todos los procesos terminaron.");
    }
}
