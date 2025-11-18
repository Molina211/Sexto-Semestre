package ReemplazoDePagina;

import java.util.*;

// Clase principal que simula el algoritmo de reemplazo de página FIFO
public class FIFO {
    public static void main(String[] args) {
        // Secuencia de referencias a páginas (simula las páginas que se solicitan)
        int[] secuencia = {7, 0, 1, 2, 0, 3, 0, 4};

        int marcos = 3; // Número de marcos de memoria disponibles

        // Usamos una cola para representar los marcos de memoria (FIFO: First In, First Out)
        Queue<Integer> memoria = new LinkedList<>();

        System.out.println("FIFO - Reemplazo de página:");

        // Recorremos cada página solicitada en la secuencia
        for (int pagina : secuencia) {
            // Si la página NO está en memoria, debemos cargarla
            if (!memoria.contains(pagina)) {
                // Si la memoria está llena (alcanzó el número de marcos)
                if (memoria.size() == marcos) {
                    memoria.poll(); // Sacamos la página más antigua (la que llegó primero)
                }
                memoria.add(pagina); // Añadimos la nueva página
            }

            // Mostramos el estado actual de la memoria después de cada acceso
            System.out.println(memoria);
        }
    }
}
