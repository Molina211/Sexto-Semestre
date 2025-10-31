# Direccionamiento IP

---

## IPv4

Se divide en 5 clases:

- A - Unicast

- B - Unicast

- C - Unicast

- D - Multicast

- E - Experimental

Estructura de la IPv4 **x.x.x.x** dada con un numero maximo de 4 millones de direcciones y un valor maximo de 255 valores.

### Asiganción del direccionamiento

- Dirección: 180.100.10.0

- Máscara: 255.255.255.0

- Prefijo: 180.100.10.3/24 - El 24 tambien se llama longitud del prefijo.

- Visualización del prefijo: 11111111.11111111.11111111.00000000 = 24 unos

Conversión a decimal:

| ------------ | 180      | 100      | 10       | 0        | -------------------- |
| ------------ |:--------:|:--------:|:--------:|:--------:|:--------------------:|
| Dirección    | 10110100 | 01100100 | 00001010 | 00000000 | 180.100.10.3         |
| Máscara      | 11111111 | 11111111 | 11111111 | 00000000 | 255.255.255.0        |

Máscaras posibles fuera del octeto:

- Máscara: 255.255.255.192

- Prefijo: 180.100.10.3/26 = 26 unos

La máscara son bloques de 1 y bloques de 0 según la longitud del prefijo.

### Funcionamiento

| Rango de direccionamiento | ------------             | 180      | 100      | 10       | 0        | -------------------- |
|:-------------------------:| ------------------------ |:--------:|:--------:|:--------:|:--------:|:--------------------:|
| ------------              | Dirección                | 10110100 | 01100100 | 00001010 | 00000000 | 180.100.10.3         |
| ------------              | Máscara                  | 11111111 | 11111111 | 11111111 | 00000000 | 255.255.255.0        |
| 180.100.10.0/24           | Dirección de red         | 10110100 | 01100100 | 00001010 | 00000000 | 24                   |
| 180.100.10.1/24           | 1<sup>ra</sup> IP valida | 10110100 | 01100100 | 00001010 | 00000001 | 1                    |
| 180.100.10.254/24         | Ultima IP valida         | 10110100 | 01100100 | 00001010 | 11111110 | 254                  |
| 180.100.10.255/24         | Dirección Broadcast      | 10110100 | 01100100 | 00001010 | 11111111 | 255                  |

La porción de red se le llama los numero de 180 hasta el 10, donde se parte con un slash entre el 10 y el 0, la porción de Host es como se le llama a la parte despues de slash, donde en este caso se ubica el 0.

- **Porción de red**

| 10110100 | 01100100 | 00001010 |
|:--------:|:--------:|:--------:|
| 180      | 100      | 10       |

- **Porción de Host**

| 00000000 |
|:--------:|
| 0        |

*Nota: La porción de Host siempre tiene un bloque de 0 en la dirección de red*

Los bloques de Ceros de la porción de Host indica la cantidad de dispositivos que se pueden conectar a esa red. La formula es 2<sup>n</sup> - 2 ----- 2<sup>8</sup> - 2 = 254 (Explicar a GPT)

**Prefijo:** Es la parte del direccionamiento del bloque que no ccambia ni varía. La misma porción de red es el prefijo. (Explicar a GPT)

**Primera IP valida:** Es aquella que tiene puros ceros menos el ultimo es 1.

**Ultima IP valida:** Es aquella que tiene puros unos menos el ultimo que es 0.

**Dirección broadcast:** Es aquella que tiene putos unos.

### EJERCICIO

200.196.160.0/20

| Rango de direccionamiento | --------------           | 200      | 196      | 160      | 2        | -------------------- |
|:-------------------------:| ------------------------ |:--------:|:--------:|:--------:|:--------:|:--------------------:|
| ------------              | Dirección                | 11001000 | 11000100 | 10100000 | 00000010 | 200.196.160.2        |
| ------------              | Máscara                  | 11111111 | 11111111 | 11110000 | 00000000 | 255.255.240.0        |
| 180.100.10.0/20           | Dirección de red         | 11001000 | 11000100 | 10100000 | 00000000 | 20                   |
| 180.100.10.1/20           | 1<sup>ra</sup> IP valida | 11001000 | 11000100 | 10100000 | 00000001 | 1                    |
| 180.100.10.254/20         | Ultima IP valida         | 11001000 | 11000100 | 10100000 | 11111110 | 4094                 |
| 180.100.10.255/20         | Dirección Broadcast      | 11001000 | 11000100 | 10100000 | 11111111 | 4095                 |
