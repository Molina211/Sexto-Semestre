package PlanificacionDeDisco;

import java.util.*;

// Clase principal que simula el algoritmo de planificación de disco SSTF
public class SSTF {
    public static void main(String[] args) {
        int cabeza = 50; // Posición inicial del cabezal del disco
        int[] solicitudes = {82, 170, 43, 140, 24, 16, 190}; // Secuencia de solicitudes de sectores/pistas

        // Convertimos el arreglo de solicitudes en una lista para poder eliminar elementos fácilmente
        List<Integer> lista = new ArrayList<>();
        for (int s : solicitudes) lista.add(s);

        System.out.println("SSTF - Planificación de disco:");

        // Mientras haya solicitudes pendientes
        while (!lista.isEmpty()) {
            int minDist = Integer.MAX_VALUE; // Inicializamos la distancia mínima
            int index = -1; // Índice de la solicitud más cercana

            // Buscamos la solicitud más cercana a la posición actual del cabezal
            for (int i = 0; i < lista.size(); i++) {
                int dist = Math.abs(lista.get(i) - cabeza); // Distancia al cabezal
                if (dist < minDist) {
                    minDist = dist; // Actualizamos la distancia mínima
                    index = i;       // Guardamos el índice de la solicitud más cercana
                }
            }

            // Mostramos el movimiento del cabezal hacia la solicitud más cercana
            System.out.println("Mover de " + cabeza + " a " + lista.get(index));

            // Actualizamos la posición del cabezal
            cabeza = lista.get(index);

            // Eliminamos la solicitud ya atendida
            lista.remove(index);
        }
    }
}


