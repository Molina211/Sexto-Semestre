# Módulo 10 - Configuración básica de un router

---

## Contenido

- **Configuración de los parámetros iniciales del router:** Configura los parámetros iniciales en un router con IOS de Cisco.

- **Configuración de interfaces:** Configura dos interfaces activas en un router con Cisco IOS.

- **Configuración del gateway predeterminado:** Configura dispositivos para utilizar el gateway predeterminado.

---

### Configuración de los parámetros iniciales del router

Las siguientes tareas deben completarse al configurar la configuración inicial en un enrutador.



1. Configure el nombre del dispositivo.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-10-27-09-40-41-image.png)

2. Proteja el modo EXEC con privilegios.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-10-27-09-41-01-image.png)

3. Proteger el modo EXEC de usuario

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-10-27-09-41-21-image.png)

4. Proteger el acceso remoto por Telnet y SSH

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-10-27-09-41-41-image.png)

5. Proteja todas las contraseñas del archivo de configuración

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-10-27-09-41-57-image.png)

6. Proporcione una notificación legal.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-10-27-09-42-15-image.png)

7. Guarde la configuración.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-10-27-09-42-32-image.png)



### Configuración básica de un router

En este ejemplo, el router R1 del diagrama de topología se configurará con la configuración inicial.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-09-43-44-image.png" title="" alt="" data-align="center">

Para configurar el nombre del dispositivo para R1, utilice los siguientes comandos .

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-09-44-01-image.png" title="" alt="" data-align="center">

*Nota: Observe cómo el indicador del enrutador muestra ahora el nombre de host del enrutador.*

Todo el acceso al router debe estar asegurado. El modo EXEC privilegiado proporciona al usuario acceso completo al dispositivo y su configuración. Por lo tanto, es el modo más importante para asegurar.

Los siguientes comandos aseguran el modo EXEC privilegiado y el modo EXEC de usuario, habilitan el acceso remoto Telnet y SSH y cifran todas las contraseñas de texto sin formato (es decir, EXEC de usuario y línea VTY).

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-09-46-56-image.png" title="" alt="" data-align="center">

La notificación legal advierte a los usuarios que solo deben acceder al dispositivo los usuarios permitidos. La notificación legal se configura de la siguiente manera.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-09-47-37-image.png" title="" alt="" data-align="center">

Si se configuraron los comandos anteriores y el router perdió energía accidentalmente, se perderían todos los comandos configurados. Por esta razón, es importante guardar la configuración cuando se implementen los cambios. Los siguientes comandos guardan la configuración en ejecución en la NVRAM.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-09-48-08-image.png" title="" alt="" data-align="center">

---

### Configuración de interfaces

Una vez completada la configuración básica, se deben configurar las interfaces del router, ya que sin ellas los dispositivos finales no pueden comunicarse con él. Los routers Cisco, como el ISR 4321, cuentan con interfaces GigabitEthernet (por ejemplo, G0/0/0 y G0/0/1). Su configuración es similar a la de un SVI en un switch, e implica usar comandos específicos para asignar direcciones IP y activar las interfaces.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-09-58-39-image.png" title="" alt="" data-align="center">

1. **Interface type-and-number**

**Función:** 
Permite entrar al modo de configuración de una interfaz específica del router (por ejemplo, `GigabitEthernet0/0` o `Serial0/1/0`). 
**Ejemplo:** `interface GigabitEthernet0/0`

2. **Description description-text**

**Función:** 
Agrega una descripción informativa sobre la interfaz. 
Sirve para identificar su uso o conexión (por ejemplo, “Conexión a ISP principal”). 
**Nota:** Máximo 240 caracteres.

3. **Ip address ipv4-address subnet-mask**

**Función:** 
Asigna una dirección IPv4 y su máscara de subred a la interfaz. 
**Ejemplo:** `ip address 192.168.1.1 255.255.255.0`

4. **Ipv6 address ipv6-address/prefix-length**

**Función:** 
Asigna una dirección IPv6 a la interfaz. 
**Ejemplo:** `ipv6 address 2001:db8::1/64`

5. **no shutdown**

**Función:** 
Habilita la interfaz (la “enciende”). 
Por defecto, muchas interfaces están apagadas, y este comando las activa para que puedan transmitir datos.

*Nota:*

- Al habilitar una interfaz, el router muestra mensajes confirmando la conexión.

- `description` no es obligatorio, pero ayuda en redes grandes a identificar conexiones.

- `no shutdown` es necesario para activar la interfaz físicamente.

- En enlaces entre routers (sin switch intermedio), ambas interfaces deben configurarse y activarse.



#### Ejemplo de Configuración de interfaces de routers

En este ejemplo, se habilitarán las interfaces directamente conectadas de R1 en el diagrama de topología.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-06-36-image.png" title="" alt="" data-align="center">

Para configurar las interfaces en R1, utilice los siguientes comandos.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-07-03-image.png" title="" alt="" data-align="center">

*Nota: Observe los mensajes informativos que nos informan de que G0/0/0 y G0/0/1 están activados.*



#### Verificación de configuración de interfaz

Existen varios comandos que se pueden utilizar para verificar la configuración de interfaz. El más útil de estos es el comando `show ip interface brief` y `show ipv6 interface brief`, como se muestra en el ejemplo.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-08-12-image.png" title="" alt="" data-align="center">

#### Configuración comandos de Verificación

En la tabla se resumen los comandos `show` más populares utilizados para verificar la configuración de la interfaz.

| **Comando**                                               | **Descripción**                                                                                                                                                                                                                                             |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **show ip interface brief** **show ipv6 interface brief** | Muestra todas las interfaces, sus direcciones IP y su estado actual. Las interfaces configuradas y conectadas deben mostrar un estado de «up» (arriba) y un protocolo de «up». Cualquier otro estado indica un problema con la configuración o el cableado. |
| **show ip route** **show ipv6 route**                     | Muestra el contenido de la tabla de enrutamiento IP que se almacena en la memoria RAM.                                                                                                                                                                      |
| **show interfaces**                                       | Muestra estadísticas de todas las interfaces del dispositivo. Sin embargo, este comando solo mostrará la información de direccionamiento IPv4.                                                                                                              |
| **show ip interfaces**                                    | Muestra las estadísticas de IPv4 correspondientes a todas las interfaces de un router.                                                                                                                                                                      |
| **show ipv6 interface**                                   | Muestra las estadísticas de IPv6 correspondientes a todas las interfaces de un router.                                                                                                                                                                      |

1. **Show ip interface brief**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-13-04-image.png" title="" alt="" data-align="center">

2. **Show ipv6 interface brief**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-13-49-image.png" title="" alt="" data-align="center">

3. **Show ip route**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-14-09-image.png" title="" alt="" data-align="center">

4. **Show ipv6 route**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-14-47-image.png" title="" alt="" data-align="center">

5. **Show interfaces**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-15-19-image.png" title="" alt="" data-align="center">

6. **Show ip interface**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-17-02-image.png" title="" alt="" data-align="center">

7. **Show ipv6 interface**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-17-38-image.png" title="" alt="" data-align="center">

---

### Configuración del gateway predeterminado

El gateway predeterminado (puerta de enlace) es el router que permite a los dispositivos de una red comunicarse con otras redes. 
Cada host debe configurarse con una dirección IP y la dirección del gateway correspondiente, que normalmente es la de la interfaz del router conectada a su misma red. 
Si hay varios routers, se elige uno como puerta de enlace predeterminada. 
El gateway solo se usa cuando el destino está fuera de la red local; si el destino está en la misma red (como entre dos PCs de una misma LAN), el tráfico se envía directamente sin pasar por el router.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-21-13-image.png" title="" alt="" data-align="center">

Si PC1 envía un paquete a PC3 (que está en otra red), el paquete se envía al gateway predeterminado (R1). El router revisa su tabla de enrutamiento para decidir por qué interfaz debe reenviar el paquete y lo envía hacia PC3 por la ruta adecuada.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-21-59-image.png" title="" alt="" data-align="center">

El mismo proceso ocurriría en una red IPv6, aunque esto no se muestra en la topología. Los dispositivos usarían la dirección IPv6 del enrutador local como puerta de enlace predeterminada.



#### Gateway predeterminado para un switch

Un switch de capa 2 no necesita dirección IP para funcionar, pero sí puede configurarse una para permitir la administración remota. 
Esto se logra mediante una interfaz virtual de switch (SVI) con dirección IPv4 y máscara de subred. 
Además, se debe configurar un gateway predeterminado (con el comando `ip default-gateway [dirección IP]`), que corresponde a la interfaz del router conectada al switch. 
Así, el administrador puede acceder y gestionar el switch desde otra red.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-27-10-23-46-image.png" title="" alt="" data-align="center">

Cuando un host administrador accede a un switch remoto, el tráfico pasa por el router (R1), por lo que el switch S1 necesita una puerta de enlace predeterminada configurada para poder responder y establecer la conexión SSH. 
Los servidores conectados al switch ya deben tener su gateway configurado en su sistema operativo. 
En redes IPv6, el switch puede obtener automáticamente su puerta de enlace predeterminada mediante los mensajes ICMPv6 Router Advertisement, sin necesidad de configurarla manualmente.


