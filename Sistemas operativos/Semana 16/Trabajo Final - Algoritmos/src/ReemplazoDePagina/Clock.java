package ReemplazoDePagina;

import java.util.*;

// Clase principal que simula el algoritmo de reemplazo de página Clock
public class Clock {
    public static void main(String[] args) {
        // Secuencia de referencias a páginas
        int[] secuencia = {7, 0, 1, 2, 0, 3, 0, 4};

        int marcos = 3; // Número de marcos de memoria disponibles

        // Arreglo que representa los marcos de memoria
        int[] memoria = new int[marcos];
        // Arreglo que indica si cada página tiene bit de uso (segunda oportunidad)
        boolean[] usado = new boolean[marcos];

        // Inicializamos memoria con -1 (vacía)
        Arrays.fill(memoria, -1);

        int puntero = 0; // Puntero del "reloj"

        System.out.println("Clock - Reemplazo de página:");

        // Recorremos cada página solicitada en la secuencia
        for (int pagina : secuencia) {
            boolean encontrada = false;

            // Revisamos si la página ya está en memoria
            for (int i = 0; i < marcos; i++) {
                if (memoria[i] == pagina) {
                    usado[i] = true; // Damos una segunda oportunidad (bit de uso)
                    encontrada = true;
                    break;
                }
            }

            // Si la página NO está en memoria
            if (!encontrada) {
                // Buscamos un marco disponible según el algoritmo Clock
                while (usado[puntero]) {
                    usado[puntero] = false;       // Quitamos la segunda oportunidad
                    puntero = (puntero + 1) % marcos; // Movemos el puntero circularmente
                }

                // Reemplazamos la página apuntada por el puntero
                memoria[puntero] = pagina;
                usado[puntero] = true;  // Marcamos como recientemente usada
                puntero = (puntero + 1) % marcos; // Avanzamos el puntero
            }

            // Mostramos el estado actual de la memoria después de cada acceso
            System.out.println(Arrays.toString(memoria));
        }
    }
}
