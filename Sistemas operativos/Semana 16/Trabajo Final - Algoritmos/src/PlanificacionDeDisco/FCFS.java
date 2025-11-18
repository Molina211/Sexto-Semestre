package PlanificacionDeDisco;

// Clase principal que simula el algoritmo de planificación de disco FCFS
public class FCFS {
    public static void main(String[] args) {
        int cabeza = 50; // Posición inicial del cabezal del disco
        int[] solicitudes = {82, 170, 43, 140, 24, 16, 190}; // Secuencia de solicitudes de sectores/pistas

        System.out.println("FCFS - Planificación de disco:");

        // Recorremos cada solicitud de disco en orden de llegada
        for (int s : solicitudes) {
            // Mostramos el movimiento del cabezal de la posición actual a la siguiente solicitud
            System.out.println("Mover de " + cabeza + " a " + s);

            // Actualizamos la posición del cabezal a la solicitud actual
            cabeza = s;
        }
    }
}

