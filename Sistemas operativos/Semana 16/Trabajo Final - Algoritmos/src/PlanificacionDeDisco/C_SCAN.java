package PlanificacionDeDisco;

import java.util.*;

// Clase principal que simula el algoritmo de planificación de disco C-SCAN
public class C_SCAN {
    public static void main(String[] args) {
        int cabeza = 50; // Posición inicial del cabezal del disco
        int[] solicitudes = {82, 170, 43, 140, 24, 16, 190}; // Secuencia de solicitudes

        // Convertimos el arreglo en una lista para poder manipularlo
        List<Integer> lista = new ArrayList<>();
        for (int s : solicitudes) lista.add(s);

        // Ordenamos las solicitudes de menor a mayor
        Collections.sort(lista);

        // Dividimos las solicitudes en dos listas: mayores o iguales al cabezal y menores
        List<Integer> mayores = new ArrayList<>();
        List<Integer> menores = new ArrayList<>();
        for (int s : lista) {
            if (s >= cabeza) mayores.add(s);
            else menores.add(s);
        }

        System.out.println("C-SCAN - Planificación de disco:");

        // Movimiento "subiendo" hacia las solicitudes mayores
        for (int s : mayores) {
            System.out.println("Mover de " + cabeza + " a " + s);
            cabeza = s; // Actualizamos la posición del cabezal
        }

        // Cuando se llega al final, el cabezal "salta" al inicio para atender las solicitudes menores
        if (!menores.isEmpty()) {
            System.out.println("Mover de " + cabeza + " a " + menores.get(0) + " (inicio)");
            cabeza = menores.get(0);

            // Atendemos el resto de las solicitudes menores en orden ascendente
            for (int i = 1; i < menores.size(); i++) {
                System.out.println("Mover de " + cabeza + " a " + menores.get(i));
                cabeza = menores.get(i);
            }
        }
    }
}


