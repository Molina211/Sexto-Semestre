#Cree una lista de 20 numeros y haga usando el ciclo "for" las sumas sucesivas de todos los numeros.
#Que la lista se cree de forma automatica

import random

numeros = [random.randint(1, 100) for _ in range(10)]
suma = 0
for numero in numeros:
    suma += numero
    numeros.sort()
    print(f"Suma actual:{numeros} {suma}")
