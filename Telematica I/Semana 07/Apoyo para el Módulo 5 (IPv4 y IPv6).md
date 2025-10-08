# Apoyo para el Módulo 5 (IPv4 y IPv6)

---

## 1. Sistema Numérico de Soporte

### Binario

- Base **2**: Solo usa `0` y `1`.

- Cada posición representa una potencia de 2:
  
  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  |:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
  | 128           | 64            | 32            | 16            | 8             | 4             | 2             | 1             |
  | **1**         | **0**         | **1**         | **1**         | **0**         | **0**         | **1**         | **1**         |
  | 128*1         | 64*0          | 32*1          | 16*1          | 8*0           | 4*0           | 2*1           | 1*1           |
  | 128           | 0             | 32            | 16            | 0             | 0             | 2             | 1             |

Sumatoria: 128+32+16+2+1=**179**

### Decimal

- Base **10**: Usa los dígitos `0 – 9`.

### Hexadecimal

- +Base **16**: Usa `0 – 9` y `A – F`.

- Cada dígito hexadecimal equivale a **4 bits** (medio byte).

- Ejemplos:
  
  - `A` = 10 decimal = `1010` binario.
  
  - `F` = 15 decimal = `1111` binario.

| Valores de 2<sup>n</sup> | 128          | 64           | 32           | 16    | 8            | 4            | 2            | 1     | Suma                        |
| ------------------------ |:------------:|:------------:|:------------:|:-----:|:------------:|:------------:|:------------:|:-----:|:---------------------------:|
| *Byte*                   | *1*          | *0*          | *1*          | *1*   | *0*          | *0*          | *1*          | *1*   | **1 Byte**                  |
| *Hexadecimal*            | ------------ | ------------ | ------------ | *B*   | ------------ | ------------ | ------------ | *3*   | **2 digitos hexadecimales** |
| *Bits*                   | 1 bit        | 1 bit        | 1 bit        | 1 bit | 1 bit        | 1 bit        | 1 bit        | 1 bit | **8 bits en total**         |

- **1 Byte (8 bits) = 2 dígitos hexadecimales.**

---

## 2. IPv4

### Características

- Longitud: **32 bits**.
  
  | Dirección         | 192      | 168      | 10       | 10       | Suma         |
  | ----------------- |:--------:|:--------:|:--------:|:--------:|:------------:|
  | *Binario/Octetos* | 11000000 | 10101000 | 00001010 | 00001010 | ------------ |
  | *Bit totales*     | 8        | 8        | 8        | 8        | **32**       |

- Dividido en **4 octetos** de 8 bits.

- Notación decimal con puntos.

- **Rango de cada octeto**: 0 – 255. **Total de valores:** 256.

| Dirección IPv4 Max. | 255           | 255           | 255           | 255           | No se pueden valores superiores a 255 |
| ------------------- |:-------------:|:-------------:|:-------------:|:-------------:|:-------------------------------------:|
| Potenciación        | 2<sup>8</sup> | 2<sup>8</sup> | 2<sup>8</sup> | 2<sup>8</sup> | **2<sup>32</sup>**                    |
| Dirección IPv4 Min. | 0             | 0             | 0             | 0             | No se pueden valores inferiores a 0   |

- Total de direcciones:
  
  2<sup>32</sup>=4,294,967,296

### Ejemplo

| Ejemplo       | 192       | 168       | 1         | 10        |
| ------------- |:---------:|:---------:|:---------:|:---------:|
| *Binario*     | 1100 0000 | 1010 1000 | 0000 0001 | 0000 1010 |
| *Hexadecimal* | C 0       | A 8       | 0 1       | 0 8       |

### Ejemplo de conversión

Decimal → Binario:

- Valor decimal: *105*
  
  - 128 ≤ 105? ❌ → Bit 0
  
  - 64 ≤ 105? ✅ → Bit 1 → Resto: 105 - 64 = 41
  
  - 32 ≤ 41? ✅ → Bit 1 → Resto: 41 - 32 = 9
  
  - 16 ≤ 9? ❌ → Bit 0
  
  - 8 ≤ 9? ✅ → Bit 1 → Resto: 9 - 8 = 1
  
  - 4 ≤ 1? ❌  → Bit 0
  
  - 2 ≤ 1? ❌ → Bit 0
  
  - 1 ≤ 1? ✅ → Bit 1 → Resto: 1 - 1 = 0

| 128   | 64    | 32    | 16    | 8     | 4     | 2     | 1     |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| **0** | **1** | **1** | **0** | **1** | **0** | **0** | **1** |

- Resultado binario: *0110 1001*

---

- Valor decimal: *200*
  
  - 128 ≤ 200? ✅ → Bit 1 → Resto: 200 - 128 = 72
  
  - 64 ≤ 72? ✅ → Bit 1 → Resto: 72 - 64 = 8
  
  - 32 ≤ 8? ❌ → Bit 0
  
  - 16 ≤ 8? ❌ → Bit 0
  
  - 8 ≤ 8? ✅ → Bit 1 → Resto: 8 - 8 = 0
  
  - 4 ≤ 0? ❌ → Bit 0
  
  - 2 ≤ 0? ❌ → Bit 0
  
  - 1 ≤ 0? ❌ → Bit 0

| 128   | 64    | 32    | 16    | 8     | 4     | 2     | 1     |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| **1** | **1** | **0** | **0** | **1** | **0** | **0** | **0** |

- Resultado binario: *1100 1000*

---

Binario → Decimal:

- Valor binario: *10110011*

| Número binario                                       | 1             | 0             | 1             | 1             | 0             | 0             | 1             | 1             |
| ---------------------------------------------------- |:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| **Potencia de 2**                                    | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
| **Valor**                                            | 128           | 64            | 32            | 16            | 8             | 4             | 2             | 1             |
| **Bit del número binario multiplicado por su valor** | 128           | 0             | 32            | 16            | 0             | 0             | 2             | 1             |

*Nota:* La potencia a la 2 se escribe de derecha a izquierda empezando con 2<sup>0</sup>.

- Sumatoria: 128+32+16+2+1=**179**

---

- Valor binario: *11001001*

| Número binario                                       | 1             | 1             | 0             | 0             | 1             | 0             | 0             | 1             |
| ---------------------------------------------------- |:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| **Potencia de 2**                                    | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
| **Valor**                                            | 128           | 64            | 32            | 16            | 8             | 4             | 2             | 1             |
| **Bit del número binario multiplicado por su valor** | 128           | 64            | 0             | 0             | 8             | 0             | 0             | 1             |

*Nota:* La potencia a la 2 se escribe de derecha a izquierda empezando con 2<sup>0</sup>.

- Sumatoria: 128+64+8+1=**201**

---

### Direcciones especiales

| Máscara         | Nombre (Clase) | CIDR | Uso Típico                   |
| --------------- | -------------- | ---- | ---------------------------- |
| 255.255.255.255 | Broadcast      | /32  | Host específico o broadcast  |
| 255.255.255.0   | Clase C        | /24  | Redes pequeñas (hogares/ofi) |
| 255.255.0.0     | Clase B        | /16  | Redes medianas/grandes       |
| 255.0.0.0       | Clase A        | /8   | Redes enormes                |

---

## 3. IPv6

### Características

- Longitud: **128 bits**.

| Dirección         | 2001                | 0db8                | 85a3                | 0000                | 0000                | 8a2e                | 0370                | 7334                | Suma                                             |
| ----------------- |:-------------------:|:-------------------:|:-------------------:|:-------------------:|:-------------------:|:-------------------:|:-------------------:|:-------------------:|:------------------------------------------------:|
| *Binario/Octetos* | 0010 0000 0000 0001 | 0000 1101 1011 1000 | 1000 0101 1010 0011 | 0000 0000 0000 0000 | 0000 0000 0000 0000 | 1000 1010 0010 1110 | 0000 0011 0111 0000 | 0111 0011 0011 0100 | ------------------------------------------------ |
| *Bits*            | 16                  | 16                  | 16                  | 16                  | 16                  | 16                  | 16                  | 16                  | **128**                                          |

- Dividido en **8 bloques de 16 bits**.

- Cada bloque representado en **4 dígitos hexadecimales**.

- Separados por `:` (dos puntos).

- **Rango de cada bloque**: `0000 – FFFF` (0 – 65,535 decimal). **Total de valores:** 65,536.

| Dirección IPv6 Max. | FFFF           | FFFF           | FFFF           | FFFF           | FFFF           | FFFF           | FFFF           | FFFF           | No se pueden valores superiores a 65,535 |
| ------------------- |:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:----------------------------------------:|
| Valor               | 65535          | 65535          | 65535          | 65535          | 65535          | 65535          | 65535          | 65535          | **3.4×10<sup>38</sup>**                  |
| Potenciación        | 2<sup>16</sup> | 2<sup>16</sup> | 2<sup>16</sup> | 2<sup>16</sup> | 2<sup>16</sup> | 2<sup>16</sup> | 2<sup>16</sup> | 2<sup>16</sup> | **2<sup>128</sup>**                      |
| Dirección IPv6 Min. | 0000           | 0000           | 0000           | 0000           | 0000           | 0000           | 0000           | 0000           | No se pueden valores inferiores a 0      |

- Total de direcciones:
  
  2<sup>128</sup>≈3.4×10<sup>38</sup>

- Particiones:
  
  **F** = 15 → Equivale a 4 Bits
  
  **FF** = 255 → Equivale a 8 Bits → Equivale a 1 Byte
  
  **FFF** = 4095 → Equivale a 12 Bits
  
  **FFFF** = 65535 → Equivale a 16 Bits → Equivale a 2 Byte

### Ejemplo

`IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334`

- Primer bloque `2001`:

| Dígitos hexadecimales | 2    | 0    | 0    | 1    |
|:---------------------:|:----:|:----:|:----:|:----:|
| Valor binario         | 0010 | 0000 | 0000 | 0001 |

- Binario: *0010 0000 0000 0001*

| Binario | Valores        | Decimal | Multiplicar el Decimal con el Binario | Valor |
|:-------:|:--------------:|:-------:|:-------------------------------------:|:-----:|
| 0       | 2<sup>15</sup> | 32768   | 32768*0=0                             | 0     |
| 0       | 2<sup>14</sup> | 16384   | 16384*0=0                             | 0     |
| 1       | 2<sup>13</sup> | 8192    | 8192*1=8192                           | 8192  |
| 0       | 2<sup>12</sup> | 4096    | 4096*0=0                              | 0     |
| 0       | 2<sup>11</sup> | 2048    | 2048*0=0                              | 0     |
| 0       | 2<sup>10</sup> | 1024    | 1024*0=0                              | 0     |
| 0       | 2<sup>9</sup>  | 512     | 512*0=0                               | 0     |
| 0       | 2<sup>8</sup>  | 256     | 256*0=0                               | 0     |
| 0       | 2<sup>7</sup>  | 128     | 128*0=0                               | 0     |
| 0       | 2<sup>6</sup>  | 64      | 64*0=0                                | 0     |
| 0       | 2<sup>5</sup>  | 32      | 32*0=0                                | 0     |
| 0       | 2<sup>4</sup>  | 16      | 16*0=0                                | 0     |
| 0       | 2<sup>3</sup>  | 8       | 8*0=0                                 | 0     |
| 0       | 2<sup>2</sup>  | 4       | 4*0=0                                 | 0     |
| 0       | 2<sup>1</sup>  | 2       | 2*0=0                                 | 0     |
| 1       | 2<sup>0</sup>  | 1       | 1*1=1                                 | 1     |

- Sumatoria: 8192+1=**8193**

El valor del primer bloque es de **8193** en decimal.

### Ejemplo de conversión

Decimal → Hexadecimal:

- Valor decimal: *4055*
  
  - 2048 ≤ 4055? ✅ → Bit 1 → Resto: 4055 - 2048 = 2007
  
  - 1024 ≤ 2007? ✅ → Bit 1 → Resto: 2007 - 1024 = 983
  
  - 512 ≤ 983? ✅ → Bit 1 → Resto: 983 - 512 = 471
  
  - 256 ≤ 471? ✅ → Bit 1 → Resto: 471 - 256 = 215
  
  - 128 ≤ 215? ✅ → Bit 1 → Resto: 215 - 128 = 87
  
  - 64 ≤ 87? ✅ → Bit 1 → Resto: 87 - 64 = 23
  
  - 32 ≤ 23? ❌ → Bit 0
  
  - 16 ≤ 23? ✅ → Bit 1 → Resto: 23 - 16 = 7
  
  - 8 ≤ 7? ❌ → Bit 0
  
  - 4 ≤ 7? ✅ → Bit 1 → Resto: 7 - 4 = 3
  
  - 2 ≤ 3? ✅ → Bit 1 → Resto: 3 - 2 = 1
  
  - 1 ≤ 1? ✅ → Bit 1 → Resto: 1 - 1 = 0

| 2048  | 1024  | 512   | 256   | 128   | 64    | 32    | 16    | 8     | 4     | 2     | 1     |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **1** | **1** | **1** | **1** | **1** | **1** | **0** | **1** | **0** | **1** | **1** | **1** |

- Resultado binario: *111111010111*

Se separa en grupos de 4 bits para una mejor comprensión: 1111 1101 0111

Luego, se convierte cada bloque de 4 bits en su representación en hexadecimal de izquierda a derecha.

- Resultado hexadecimal: ***F**(1111) **D**(1101) **7**(0111)* = *FD7*

### Reglas de simplificación

1. Omitir ceros a la izquierda:
   
   `2001:0db8:0000:0000:0000:0000:0000:0001 → 2001:db8::1`

2. Usar `::` una sola vez para varios bloques `0000`.

---

## 4. Comparación IPv4 vs IPv6

| Característica       | IPv4                    | IPv6                       |
| -------------------- | ----------------------- | -------------------------- |
| Tamaño en bits       | 32                      | 128                        |
| Número de bloques    | 4 (octetos)             | 8 (bloques)                |
| Tamaño de bloque     | 8 bits                  | 16 bits                    |
| Representación       | Decimal con puntos      | Hexadecimal con dos puntos |
| Rango por bloque     | 0 – 255                 | 0000 – FFFF (0 – 65,535)   |
| Total de direcciones | 2^32 ≈ 4.3 mil millones | 2^128 ≈ 340 sextillones    |
| Ejemplo              | 192.168.1.1             | 2001:db8::1                |
