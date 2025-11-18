package ReemplazoDePagina;

import java.util.*;

// Clase principal que simula el algoritmo de reemplazo de página LFU
public class LFU {
    public static void main(String[] args) {
        // Secuencia de referencias a páginas
        int[] secuencia = {7, 0, 1, 2, 0, 3, 0, 4};

        int marcos = 3; // Número de marcos de memoria disponibles

        // Lista para representar los marcos de memoria
        List<Integer> memoria = new ArrayList<>();

        // Mapa para almacenar la frecuencia de uso de cada página
        Map<Integer, Integer> frecuencia = new HashMap<>();

        System.out.println("LFU - Reemplazo de página:");

        // Recorremos cada página solicitada en la secuencia
        for (int pagina : secuencia) {
            // Incrementamos la frecuencia de la página (si no existía, se inicia en 0)
            frecuencia.put(pagina, frecuencia.getOrDefault(pagina, 0) + 1);

            // Si la página NO está en memoria, debemos cargarla
            if (!memoria.contains(pagina)) {
                // Si la memoria está llena
                if (memoria.size() == marcos) {
                    int minFreq = Integer.MAX_VALUE; // Inicializamos la mínima frecuencia
                    int reemplazar = -1; // Página a reemplazar

                    // Buscamos la página con menor frecuencia de uso
                    for (int m : memoria) {
                        if (frecuencia.get(m) < minFreq) {
                            minFreq = frecuencia.get(m);
                            reemplazar = m;
                        }
                    }

                    // Removemos la página menos utilizada (LFU)
                    memoria.remove((Integer) reemplazar);
                }

                // Agregamos la nueva página a la memoria
                memoria.add(pagina);
            }

            // Mostramos el estado actual de la memoria después de cada acceso
            System.out.println(memoria);
        }
    }
}

