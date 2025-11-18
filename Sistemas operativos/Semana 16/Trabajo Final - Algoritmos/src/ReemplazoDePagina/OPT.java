package ReemplazoDePagina;

import java.util.*;

// Clase principal que simula el algoritmo de reemplazo de página OPT (Óptimo)
public class OPT {
    public static void main(String[] args) {
        // Secuencia de referencias a páginas (simula las páginas que se solicitan)
        int[] secuencia = {7, 0, 1, 2, 0, 3, 0, 4};

        int marcos = 3; // Número de marcos de memoria disponibles

        // Usamos una lista para representar los marcos de memoria
        List<Integer> memoria = new ArrayList<>();

        System.out.println("OPT - Reemplazo de página:");

        // Recorremos cada página solicitada en la secuencia
        for (int i = 0; i < secuencia.length; i++) {
            int pagina = secuencia[i];

            // Si la página NO está en memoria, debemos cargarla
            if (!memoria.contains(pagina)) {
                // Si la memoria está llena
                if (memoria.size() == marcos) {
                    int indexReemplazar = -1; // Índice de la página a reemplazar
                    int maxDist = -1; // Distancia más lejana a su próximo uso

                    // Buscamos qué página se usará más tarde en el futuro
                    for (int j = 0; j < memoria.size(); j++) {
                        int proximaUso = Integer.MAX_VALUE; // Asumimos que no se usará más
                        for (int k = i + 1; k < secuencia.length; k++) {
                            if (secuencia[k] == memoria.get(j)) {
                                proximaUso = k; // Guardamos la próxima posición donde se usará
                                break;
                            }
                        }
                        // Elegimos la página que se usará más tarde (o nunca)
                        if (proximaUso > maxDist) {
                            maxDist = proximaUso;
                            indexReemplazar = j;
                        }
                    }

                    // Reemplazamos la página seleccionada
                    memoria.remove(indexReemplazar);
                }

                // Agregamos la nueva página a la memoria
                memoria.add(pagina);
            }

            // Mostramos el estado actual de la memoria después de cada acceso
            System.out.println(memoria);
        }
    }
}
