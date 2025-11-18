package ReemplazoDePagina;

import java.util.*;

// Clase principal que simula el algoritmo de reemplazo de página LRU
public class LRU {
    public static void main(String[] args) {
        // Secuencia de referencias a páginas (simula las páginas que se solicitan)
        int[] secuencia = {7, 0, 1, 2, 0, 3, 0, 4};

        int marcos = 3; // Número de marcos de memoria disponibles

        // Usamos una lista para representar los marcos de memoria
        // La posición en la lista representa el orden de uso (la más reciente se agrega al final)
        List<Integer> memoria = new ArrayList<>();

        System.out.println("LRU - Reemplazo de página:");

        // Recorremos cada página solicitada en la secuencia
        for (int pagina : secuencia) {
            if (memoria.contains(pagina)) {
                // Si la página ya está en memoria, la removemos para actualizar su posición
                // Esto asegura que quede como la más recientemente usada
                memoria.remove((Integer) pagina);
            } else if (memoria.size() == marcos) {
                // Si la página NO está en memoria y la memoria está llena
                // Eliminamos la página menos recientemente usada (la primera de la lista)
                memoria.remove(0);
            }
            // Agregamos la página al final de la lista (la más recientemente usada)
            memoria.add(pagina);

            // Mostramos el estado actual de la memoria después de cada acceso
            System.out.println(memoria);
        }
    }
}

