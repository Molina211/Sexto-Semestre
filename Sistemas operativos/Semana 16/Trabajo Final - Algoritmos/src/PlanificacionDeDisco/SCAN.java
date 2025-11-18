package PlanificacionDeDisco;

import java.util.*;

// Clase principal que simula el algoritmo de planificación de disco SCAN
public class SCAN {
    public static void main(String[] args) {
        int cabeza = 50; // Posición inicial del cabezal del disco
        int[] solicitudes = {82, 170, 43, 140, 24, 16, 190}; // Secuencia de solicitudes de pistas

        // Convertimos el arreglo en una lista para poder manipularlo
        List<Integer> lista = new ArrayList<>();
        for (int s : solicitudes) lista.add(s);

        // Ordenamos las solicitudes de menor a mayor
        Collections.sort(lista);

        // Dividimos las solicitudes en dos listas: mayores o iguales al cabezal y menores
        List<Integer> mayores = new ArrayList<>(); // Hacia donde se mueve inicialmente (subiendo)
        List<Integer> menores = new ArrayList<>(); // Luego se mueve en sentido contrario (bajando)

        for (int s : lista) {
            if (s >= cabeza) mayores.add(s);
            else menores.add(s);
        }

        System.out.println("SCAN - Planificación de disco:");

        // Movimiento "subiendo" hacia las solicitudes mayores
        for (int s : mayores) {
            System.out.println("Mover de " + cabeza + " a " + s);
            cabeza = s; // Actualizamos la posición del cabezal
        }

        // Movimiento "bajando" hacia las solicitudes menores
        Collections.reverse(menores); // Revertimos para moverse en orden descendente
        for (int s : menores) {
            System.out.println("Mover de " + cabeza + " a " + s);
            cabeza = s;
        }
    }
}
