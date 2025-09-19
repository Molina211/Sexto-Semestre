# Módulo 5: Sistemas numéricos

---

## Contenido

- **Sistema de numeración binaria:** Cálculo de los números entre los sistemas decimales y binarios.
- **Sistema de numeración hexadecimal:** Cálculo de los números entre los sistemas decimales y hexadecimales.

---

### Sistema de numeración binaria

Las direcciones IPv4 se representan en **binario (1 y 0)**, pero como son difíciles de manejar, los administradores las convierten a **decimal (0–9)**. Comprender el sistema binario es fundamental porque los dispositivos de red (hosts, servidores y routers) usan direcciones IPv4 binarias para identificarse y comunicarse.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-17-10-36-46-image.png" title="" alt="" data-align="center">

Una dirección IPv4 tiene 32 bits divididos en 4 octetos de 8 bits separados por puntos. Aunque los dispositivos usan direcciones en binario, para los humanos se representan en notación decimal con puntos.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-17-10-38-04-image.png" title="" alt="" data-align="center">

#### Notación de posición binaria

*Notación decimal base en 10*

Las viñetas siguientes describen cada fila de la tabla.

- **Fila 1:** Radix es la base numérica. La notación decimal se basa en 10, por lo tanto, la raíz es 10.

- **Fila 2:** Posición en número considera la posición del número decimal que comienza con, de derecha a izquierda, 0 (1ª posición), 1 (2ª posición), 2 (3ª posición), 3 (4ª posición). Estos números también representan el valor exponencial utilizado para calcular el valor posicional en la cuarta fila.

- **Fila 3:** Calcula el valor posicional tomando la raíz y elevándola por el valor exponencial de su posición en la fila 2.  

- **Fila 4:** Representa unidades de miles, cientos, decenas y unos.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-17-11-11-18-image.png" title="" alt="" data-align="center">

**EJEMPLO:**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-17-11-14-52-image.png" title="" alt="" data-align="center">

*Notación binaria base en 2*

Las viñetas siguientes describen cada fila de la tabla.

- **Fila 1:** Radix es la base numérica. La notación binaria se basa en 2, por lo tanto, el radix es 2.

- **Fila 2:** Posición en número considera la posición del número binario que comienza con, de derecha a izquierda, 0 (1ª posición), 1 (2ª posición), 2 (3ª posición), 3 (4ª posición). Estos números también representan el valor exponencial utilizado para calcular el valor posicional en la cuarta fila.

- **Fila 3:** Calcula el valor posicional tomando la raíz y elevándola por el valor exponencial de su posición en la fila 2.  

- **Fila 4:** Representa unidades de uno, dos, cuatro, ocho, etc.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-17-11-18-27-image.png" title="" alt="" data-align="center">

**EJEMPLO:**

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-09-17-11-19-06-image.png)

#### Convertir binario a decimal

###### ChatGPT dijo:

Para convertir una dirección IPv4 en binario a su equivalente decimal punteado:

1. Se divide la dirección en 4 octetos de 8 bits.

2. Cada octeto se convierte a decimal aplicando los valores de posición binaria (128, 64, 32, 16, 8, 4, 2, 1).

3. El resultado de cada conversión forma los cuatro números de la dirección decimal.

**EJEMPLOS**

Suponga que 11000000.10101000.00001011.00001010 es la dirección IPv4 binaria de un host. Para convertir la dirección binaria a decimal, comience con el primer octeto. Introduzca el número binario de 8 bits en el valor de posición de la fila 1 y, después, calcule para producir el número decimal 192. Este número entra en el primer octeto de la notación decimal punteada.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-18-10-54-24-image.png" title="" alt="" data-align="center">

A continuación, convertir el segundo octeto de 10101000. El valor decimal resultante es 168 y entra en el segundo octeto.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-18-10-54-52-image.png" title="" alt="" data-align="center">

Convertir el tercer octeto de 00001011 como se muestra en la tabla.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-18-10-55-07-image.png" title="" alt="" data-align="center">

Convertir el cuarto octeto de 00001010 como se muestra en la tabla. Esto completa la dirección IP y produce **192.168.11.10**.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-18-10-55-27-image.png" title="" alt="" data-align="center">

#### Conversión de sistema decimal a binario

El método decimal a binario para cada octeto de una dirección IPv4 se basa en ir comparando el número decimal con los valores de los bits (potencias de 2):

**Pasos del método:**

1. Toma el número decimal del octeto (entre 0 y 255).

2. Compáralo con el valor más alto (128).
   
   - Si es **mayor o igual**, escribe `1` y resta ese valor al número.
   
   - Si es **menor**, escribe `0` y sigues con el mismo número.

3. Repite el proceso con los siguientes valores: 64, 32, 16, 8, 4, 2 y 1.

4. Al final tendrás 8 bits (0 o 1) que representan el octeto en binario.

---

**Ejemplo: convertir `192` a binario**

- ¿192 ≥ 128? → Sí → pongo `1` → 192 - 128 = 64

- ¿64 ≥ 64? → Sí → pongo `1` → 64 - 64 = **0**

- ¿0 ≥ 32? → No → pongo `0`

- ¿0 ≥ 16? → No → pongo `0`

- ¿0 ≥ 8? → No → pongo `0`

- ¿0 ≥ 4? → No → pongo `0`

- ¿0 ≥ 2? → No → pongo `0`

- ¿0 ≥ 1? → No → pongo `0`

Resultado: **11000000**



#### Direcciones IPv4

Los routers y computadoras entienden binario**, mientras que los humanos usamos decimal. Por eso es clave dominar ambos sistemas y su aplicación en redes.

- **Dirección en formato decimal punteado:** 192.168.10.10 es una dirección IP asignada a una computadora.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-18-11-26-31-image.png" title="" alt="" data-align="center">

- **Octetos:** La dirección se compone de cuatro octetos diferentes.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-18-11-27-51-image.png" title="" alt="" data-align="center">

- **Dirección de 32 bits:** La computadora almacena la dirección como el flujo de datos total de 32 bits.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-18-11-28-24-image.png" title="" alt="" data-align="center">

---

### Sistema numérico hexadecimal

El decimal es base 10 y el hexadecimal es base 16, usando los dígitos 0–9 y las letras A–F. Cada grupo binario de 4 bits (0000–1111) tiene un equivalente en decimal y en hexadecimal.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-18-12-06-02-image.png" title="" alt="" data-align="center">

El hexadecimal simplifica la representación del binario, ya que 4 bits = 1 dígito hexadecimal.

En redes se usa para:

- **Direcciones IPv6** (128 bits → 32 dígitos hex).

- **Direcciones MAC** (48 bits).

En IPv6, el formato es: 
`x:x:x:x:x:x:x:x` 
Cada x = 1 hexteto = 16 bits = 4 dígitos hexadecimales.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-18-12-12-59-image.png" title="" alt="" data-align="center">

#### Conversiones decimales a hexadecimales

- **Convierte el número decimal a binario (8 bits).**
  
  - 168 en binario = `10101000`.

- **Agrupa el binario en bloques de 4 bits (desde la derecha).**
  
  - `10101000` → `1010` | `1000`.

- **Convierte cada grupo de 4 bits a su equivalente hexadecimal.**
  
  - `1010` en binario = A en hex.
  
  - `1000` en binario = 8 en hex.

168 (decimal) = A8 (hexadecimal).



#### Conversión hexadecimal a decimal

1. **Convierte cada dígito hexadecimal a 4 bits binarios.**
   
   - `D` = **1101**
   
   - `2` = **0010**

2. **Une los grupos de 4 bits en una cadena de 8 bits.**
   
   - `11010010`

3. **Convierte el binario a decimal usando valores de posición (128, 64, 32, 16, 8, 4, 2, 1).**
   
   - `11010010` = 128 + 64 + 16 + 2 = 210
