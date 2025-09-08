# =============================
# FASE 5: Loops for y while
# =============================
import random

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

N = 100
paquetes = [20, 0, 50, -5, 30, 10, 90, 0, 15, 5, 60, 40, 0, 25]
buffer = []
total = 0

for p in paquetes:
    if p <= 0:
        continue
    if total + p > N:
        print("Enviando buffer:", buffer)
        buffer = []
        total = 0
    buffer.append(p)
    total += p

if buffer:
    print("Enviando buffer final:", buffer)


MAX_TAREAS = 100

num_tareas = random.randint(5, MAX_TAREAS)

tareas = [
    {
        "id": i + 1,
        "prioridad": random.randint(1, 5),
        "tiempo": random.randint(1, 10)
    }
    for i in range(num_tareas)
]

umbral = 2

print(f"Se generaron {len(tareas)} tareas (máximo {MAX_TAREAS}).")

ronda = 1
while tareas:
    print(f"\n--- Ronda {ronda} ---")
    ejecutadas = False

    for tarea in tareas[:]:
        if tarea["prioridad"] >= umbral:
            ejecutadas = True
            print(f"Ejecutando tarea {tarea['id']} (prioridad {tarea['prioridad']}, tiempo restante {tarea['tiempo']})")
            
            tarea["tiempo"] -= 1
            if tarea["tiempo"] <= 0:
                print(f"Tarea {tarea['id']} completada")
                tareas.remove(tarea)
        else:
            print(f"Tarea {tarea['id']} eliminada (prioridad {tarea['prioridad']} < umbral {umbral})")
            tareas.remove(tarea)

    if not ejecutadas and tareas:
        print("Esperando nuevas tareas...")

    ronda += 1

print("\n Todas las tareas completadas")