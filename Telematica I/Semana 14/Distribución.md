# Personal
- 150 - Desarrollo de Software
- 130 - Diseño 3D y Animación
- 100 - QA y Testing
- *380* - *Desarrollo*

- 90 - Infraestructura y Soporte TIC (incluyendo servidores)
- 70 - Marketing y Publicación de Juegos
- 50 - Administración y Recursos Humanos
- *210* - *Administración*

- **590** - **Total de sectores de trabajo**
# Bloque IP inicial

## $100.140.80.0/22$

| Rango de direccionamiento |                          |   100    |   140    |     80     |     0      |      |
| :-----------------------: | ------------------------ | :------: | :------: | :--------: | :--------: | :--: |
|       100.140.80.0        | Dirección de red         | 01100100 | 10001100 | 010100*00* | *00000000* |      |
|       255.255.252.0       | Máscara                  | 11111111 | 11111111 | 111111*00* | *00000000* |      |
|      100.140.80.1/22      | 1<sup>ra</sup> IP valida | 01100100 | 10001100 | 010100*00* | *00000001* |  1   |
|     100.140.83.254/22     | Ultima IP valida         | 01100100 | 10001100 | 010100*11* | *11111110* | 1023 |
|     100.140.83.255/22     | Dirección Broadcast      | 01100100 | 10001100 | 010100*11* | *11111111* | 1024 |
- $/22$ - bits de host = $32 - 22 = 10$.
- $2^{10} = 1024$ direcciones totales.
- Direcciones utilizables = $2^{11} − 2 = 1024 − 2 = 1022$ (se restan red y broadcast).

Comparación con los 590 dispositivos que se buscan cubrir:

- Hosts útiles disponibles: $1022$
- Hosts requeridos: $590$
- Direcciones libres tras asignar $1022 − 590 = 432$ direcciones sobrantes.

# Servicios

| Servicio | Función                     | Puerto         | Ubicación                        |
| -------- | --------------------------- | -------------- | -------------------------------- |
| **DHCP** | Asignar IPs automáticamente | 67/68 (UDP)    | Subred local o central con relay |
| **HTTP** | Servicio web                | 80 / 443 (TPC) | Infraestructura o DMZ            |
| **DNS**  | Resolver nombres ↔ IP       | 53 (UDP)       | Infraestructura                  |
| **FTP**  | Transferencia de archivos   | 20 / 21 (TCP)  | Infraestructura                  |
| **SMTP** | Envío de correo             | 25 / 587 (TCP) | Infraestructura                  |

# Dos redes LAN

## $100.140.80.0/22$

### LAN 1 - $100.140.80.0/23$

| Rango de direccionamiento |                          |   100    |   140    |     80     |     0      | Cantidad de dispositivos |
| :-----------------------: | ------------------------ | :------: | :------: | :--------: | :--------: | :----------------------: |
|       100.140.80.0        | Dirección de red         | 01100100 | 10001100 | 0101000*0* | *00000000* |                          |
|       255.255.254.0       | Máscara                  | 11111111 | 11111111 | 1111111*0* | *00000000* |                          |
|      100.140.80.1/23      | 1<sup>ra</sup> IP valida | 01100100 | 10001100 | 0101000*0* | *00000001* |            1             |
|     100.140.81.254/23     | Ultima IP valida         | 01100100 | 10001100 | 0101000*1* | *11111110* |           510            |
|     100.140.81.255/23     | Dirección Broadcast      | 01100100 | 10001100 | 0101000*1* | *11111111* |           512            |
### LAN 2 - $100.140.82.0/23$

| Rango de direccionamiento |                          |   100    |   140    |     82     |     0      | Cantidad de dispositivos |
| :-----------------------: | ------------------------ | :------: | :------: | :--------: | :--------: | :----------------------: |
|       100.140.82.0        | Dirección de red         | 01100100 | 10001100 | 0101001*0* | *00000000* |                          |
|       255.255.254.0       | Máscara                  | 11111111 | 11111111 | 1111111*0* | *00000000* |                          |
|      100.140.82.1/22      | 1<sup>ra</sup> IP valida | 01100100 | 10001100 | 0101001*0* | *00000001* |           513            |
|     100.140.83.254/22     | Ultima IP valida         | 01100100 | 10001100 | 0101001*1* | *11111110* |           1022           |
|     100.140.83.255/22     | Dirección Broadcast      | 01100100 | 10001100 | 0101001*1* | *11111111* |           1024           |

# Servidores

Los servidores deben estar dispuestos en la subred de Soporte TI y deben ser accesibles para cualquier equipo de la red. Cada subred debe contar con su propio servicio DHCP.

- 1 Servidor HTTP
- 1 Servidor DNS
- 1 Servidor FTP
- 1 Servidor SMTP
- 6 Servidores DHCP

# Equipos de red

Cantidad de dispositivos:

- 6 Switch 2960
- 6 Router ISR4331
- 590 dispositivos

# Software de simulación

Packet Tracer

---
