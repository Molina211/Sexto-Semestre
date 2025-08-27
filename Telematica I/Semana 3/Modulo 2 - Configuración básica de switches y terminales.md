# Modulo 2: Configuración básica de switches y terminales

---

## Contenido

- **Acceso a Cisco IOS:** Explica cómo acceder a un dispositivo Cisco IOS para propósitos de configuración.

- **Navegación IOS:** Explica cómo explorar Cisco IOS para configurar los dispositivos de red.

- **La estructura de comandos:** Describe la estructura de comandos del software Cisco IOS.

- **Configuración básica de dispositivos:** Configura un dispositivo Cisco IOS usando CLI.

- **Guardar las configuraciones:** Utiliza los comandos de IOS para guardar la configuración en ejecución.

- **Puertos y direcciones:** Explica cómo se comunican los dispositivos a través de los medios de red.

- **Configurar direccionamiento IP:** Configura un dispositivo host con una dirección IP.

- **Verificar la conectividad:** Verifica la conectividad entre dos terminales.

--- 

### Acceso a Cisco IOS

Todos los dispositivos finales y de red requieren un **sistema operativo (OS)**. Este se divide en **kernel** (controla el hardware) y **shell** (conecta al usuario con el sistema). El shell puede usarse mediante:

- **CLI (Command Line Interface):** Ligera, estable y precisa, pero exige conocimientos técnicos porque todo se hace con comandos.

- **GUI (Graphical User Interface):** Más amigable, con íconos, menús y ventanas, aunque consume más recursos y no siempre ofrece todas las funciones.

En un PC, la **GUI** permite usar el mouse, escribir texto y ver resultados en pantalla de manera intuitiva. En cambio, en redes, la **CLI** (como en Cisco IOS) se maneja con teclado, introduciendo comandos y viendo los resultados en un monitor, lo que brinda mayor control y estabilidad.

Los dispositivos Cisco ejecutan versiones específicas de Cisco IOS (como IOS XE, IOS XR y NX-OS), según el tipo de equipo y las funciones requeridas. Cada dispositivo trae un IOS básico, pero se puede actualizar para obtener más capacidades.



![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-20-30-03-image.png)



- **Método de acceso**
  
  Un switch nuevo puede reenviar tráfico y permitir comunicación entre hosts sin necesidad de configuración previa. Sin embargo, todos los switches deben configurarse y protegerse adecuadamente. Para ello, se utilizan distintos métodos:
  
  - **Consola:** Acceso físico directo mediante un puerto especial. Permite configurar el dispositivo incluso sin servicios de red activos (ideal para la configuración inicial). Requiere cable de consola y software de emulación de terminal.
  
  - **SSH (Secure Shell):** Acceso remoto seguro a la CLI a través de la red. Ofrece cifrado y autenticación, lo que lo hace el método más recomendado para administrar dispositivos en producción.
  
  - **Telnet:** Acceso remoto similar a SSH, pero inseguro porque transmite credenciales y comandos en texto plano. Solo se recomienda en entornos de laboratorio o pruebas.
  
  Algunos dispositivos también cuentan con un **puerto auxiliar heredado**, que permite acceso fuera de banda mediante una conexión telefónica y módem, sin depender de los servicios de red. Por otro lado, los programas de emulación de terminal no solo facilitan el acceso, sino que también mejoran la experiencia del usuario al permitir:
  
  - Ajustar el tamaño de la ventana.
  
  - Cambiar el tamaño de las fuentes.
  
  - Personalizar esquemas de colores.
  
  Un ejemplo de esto serian **PuTTY**, **Tera Term** o **SecureCRT,** entre otros.

---

### Navegación IOS

En los dispositivos Cisco, la CLI se organiza en modos de comando que definen el nivel de acceso y las acciones que se pueden realizar. Los dos principales son:

- **Modo EXEC del usuario (User EXEC):**
  
  - Permite ejecutar solo comandos básicos de monitoreo.
  
  - No permite cambiar la configuración del dispositivo.
  
  - Se reconoce por el símbolo **`>`** (ejemplo: `Switch>` o `Router>`).
  
  - También se le llama modo de “visualización”.

- **Modo EXEC privilegiado (Privileged EXEC):**
  
  - Da acceso a todos los comandos y funciones del dispositivo.
  
  - Permite ejecutar comandos de monitoreo avanzados y acceder a la configuración.
  
  - Se identifica por el símbolo **`#`** (ejemplo: `Switch#` o `Router#`).

---

### Modo de configuración y modos de subconfiguración

Para configurar un dispositivo Cisco, el administrador debe ingresar al *modo de configuración global (`Switch(config)#`). Desde aquí se hacen cambios que afectan la operación del dispositivo completo y se puede acceder a otros modos de subconfiguración, cada uno especializado en una parte del sistema, pero los más comunes son:

- **Modo de configuración de líneas (`Switch(config-line)#`)**  
  
  Se usa para configurar accesos como consola, SSH, Telnet o auxiliar.

- **Modo de configuración de interfaces (`Switch(config-if)#`)**  
  
  Se usa para configurar puertos del switch o interfaces de red del router.

Cada modo de la CLI se reconoce fácilmente porque el indicador del sistema (prompt) cambia.  

Ejemplo:

- `Switch(config)#` → Configuración global

- `Switch(config-line)#` → Configuración de línea

- `Switch(config-if)#` → Configuración de interfaz

**Representación paso a paso:** 

- *<u>Switch>enable ----> Switch#</u> - Para pasar del modo Usuario a Privilegiado*

- *<u>Switch#configure terminal ----> Switch(config)#</u> - Para pasar del modo Privilegiado a la Configuración Global*

- *<u>Switch(config)#interface vlan 1 ----> Switch(config-if)#</u> - Para pasar del modo Configuración Global a Configuración de interfaz*

- *<u>Switch(config)#line console 0 ----&gt; Switch(config-line)#</u> - Para pasar del modo Configuración Global a Configuración de línea



Tambien, existen demas atajos dentro de los modos de configuración que mencione anteriormente, como:

- *<u>Switch#disable ----> Switch></u> - Para pasar del modo Privilegiado al modo Usuario*

- *<u>Switch(config)#line console 0 ----> Switch(config-if)#interface FastEthernet 0/1</u> - Para pasar de Configuración de línea a Configuración de interfaz*

- *<u>Switch(config-line)#end</u> o <u>Switch(config-if)#end</u> - Para pasar de Configuración de línea o Configuración de interfaz a modo Privilegiado <u>Switch#</u>*

**Nota:** En cualquier modo de configuración se puede usar <u>exit</u> para ir saliendo de ellos gradualmente.

---

### La estructura de comandos

En Cisco IOS, cada comando tiene un formato específico y debe ejecutarse en el modo correcto. La estructura básica es:



![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-22-38-46-image.png)



- **Palabra clave (keyword):** parámetro predefinido del sistema, como `ip protocols`.

- **Argumento:** valor definido por el usuario, como `192.168.10.5`.

Después de escribir el comando completo, se presiona **Enter** para ejecutarlo.

Un comando puede requerir uno o más argumentos. Para saber cuáles son obligatorios u opcionales, se debe consultar la sintaxis del comando. En la documentación:

- **Negrita** → comandos y palabras clave literales.

- *Cursiva* → argumentos que el usuario debe proporcionar.

- [x]→ elementos opcionales.

- {x} → elementos obligatorios.

- [x {y | z}] → combina opcionalidad y opciones múltiples dentro de un mismo elemento.

Ejemplos:

- **Ping** *ip-address* → el comando es **ping** y el argumento *ip-address* lo define el usuario.

- **Traceroute** *ip-address* → similar, con **traceroute** como comando.

Si un comando es complejo, puede incluir múltiples argumentos siguiendo estas convenciones:

- <u>Switch(config-if)# **switchport port-security aging** { **static** | **time** *time* | **type** {**absolute** | **inactivity**}</u>



La CLI de IOS permite usar atajos y abreviaciones para facilitar la configuración, monitoreo y solución de problemas. Estos serian:

| **Pulsación de teclas**       | **Descripción**                                                            |
| ----------------------------- | -------------------------------------------------------------------------- |
| **Tabulación**                | Completa un nombre de comando parcial.                                     |
| **Retroceso**                 | Borra el carácter a la izquierda del cursor.                               |
| **Ctrl+D**                    | Borra el carácter donde está el cursor.                                    |
| **Ctrl+K**                    | Borra desde el cursor hasta el final de la línea de comandos.              |
| **Esc D**                     | Borra desde el cursor hasta el final de la palabra.                        |
| **Ctrl+U / Ctrl+X**           | Borra desde el cursor hasta el inicio de la línea de comandos.             |
| **Ctrl+W**                    | Borra la palabra a la izquierda del cursor.                                |
| **Ctrl+A**                    | Mueve el cursor al inicio de la línea.                                     |
| **Flecha izquierda / Ctrl+B** | Mueve el cursor un carácter hacia la izquierda.                            |
| **Esc B**                     | Mueve el cursor una palabra hacia la izquierda.                            |
| **Esc F**                     | Mueve el cursor una palabra hacia la derecha.                              |
| **Flecha derecha / Ctrl+F**   | Mueve el cursor un carácter hacia la derecha.                              |
| **Ctrl+E**                    | Mueve el cursor al final de la línea de comandos.                          |
| **Flecha arriba / Ctrl+P**    | Recupera comandos previos del historial (empezando por los más recientes). |
| **Ctrl+R / Ctrl+L**           | Refresca la línea de comandos tras un mensaje de consola.                  |

Cuando un comando en IOS muestra **más información de la que cabe en pantalla**, aparece el mensaje **“--More--”**.  
En ese momento se pueden usar estas teclas:

| **Pulsación de teclas**  | **Descripción**                                                  |
| ------------------------ | ---------------------------------------------------------------- |
| **Enter**                | Muestra la siguiente línea.                                      |
| **Barra espaciadora**    | Muestra la siguiente pantalla completa.                          |
| **Cualquier otra tecla** | Termina la visualización y regresa al modo EXEC con privilegios. |

Y para salir de la operación:

| **Pulsación de teclas** | **Descripción**                                                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Ctrl+C**              | Finaliza el modo de configuración y regresa al modo EXEC privilegiado. Si está ejecutando un comando, lo interrumpe. |
| **Ctrl+Z**              | Finaliza el modo de configuración y regresa al modo EXEC privilegiado.                                               |
| **Ctrl+Shift+6**        | Interrumpe procesos en ejecución como búsquedas DNS, traceroute, ping, etc.                                          |

---

### Configuración básica de dispositivos

En Cisco IOS, el primer paso de configuración es asignar un nombre de host único al dispositivo, ya que todos traen uno genérico de fábrica (ej. *Switch*).  

Si se dejan los nombres por defecto, sería difícil identificar los equipos, sobre todo al conectarse remotamente (SSH).

El nombre de host facilita:

- Confirmar que se está en el dispositivo correcto.

- Recordar, analizar e identificar cada equipo en la red.

Reglas para el nombre de host en IOS:

- Debe comenzar y terminar con letra o número.

- Sin espacios.

- Solo letras, números y guiones.

- Máximo 64 caracteres.

- Distingue entre mayúsculas y minúsculas.

Cada organización debe definir una convención de nombres (ejemplo: incluir ubicación y función del dispositivo) y documentarla para mantener consistencia en toda la red.



![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-23-29-29-image.png)



Para aplicar la convención de nombres en un dispositivo Cisco IOS:

1. Ingresar al modo de configuración global con: 
   
   *<u>Switch#configure terminal ----> Switch(config)#</u>*
2. Asignar un nombre de host con el comando:
   
   *<u>Switch(config)#hostname Oficina1 ----> Oficina1(config)#</u>*

Nota: Si se quiere eliminar el nombra para volver al predeterminado usa:
*<u>Oficina1(config)#no hostname ----> Switch(config)#</u>*



- **Contraseñas**
  
  
  
  -  **Pautas**
    
    El uso de contraseñas débiles es un riesgo de seguridad en dispositivos de red.
    
    Cisco IOS permite configurar contraseñas jerárquicas para distintos niveles de acceso (EXEC de usuario, EXEC privilegiado y Telnet remoto) y todas deben estar **encriptadas** y acompañadas de avisos legales.
    
    **Recomendaciones para contraseñas seguras:**
    
    - Más de 8 caracteres.
    
    - Combinar mayúsculas, minúsculas, números y símbolos.
    
    - No reutilizar la misma contraseña en todos los dispositivos.
    
    - Evitar palabras comunes.
    
    - Usar generadores de contraseñas para mayor seguridad.
  
  - **Configuración**
    
    Cuando te conectas a un dispositivo, entras en el modo EXEC de usuario.
    
    Para protegerlo, debes:
    
    ```
    Oficina1#configure terminal
    Oficina1(config)#line console 0
    Oficina1(config-line)#password ofi123
    Oficina1(config-line)#login
    Oficina1(config-line)#end
    Oficina1#
    ```
    
    Así, cada vez que alguien use la consola, deberá ingresar una contraseña antes de acceder al modo EXEC de usuario.
    
    El modo EXEC privilegiado da acceso completo a la configuración del dispositivo.
    
    Para protegerlo, se usa el comando:
    
    ```
    Oficina1# configure terminal
    Oficina1(config)# enable secret 123ofi
    Oficina1(config)# exit
    Oficina1#
    ```
    
    Esto asegura el acceso administrativo al IOS con una contraseña encriptada.
    
    Las líneas VTY son las que permiten conectarse remotamente al dispositivo usando Telnet o SSH. Los switches Cisco suelen tener 16 líneas VTY, numeradas de 0 a 15 (es decir, hasta 16 sesiones remotas al mismo tiempo).
    
    Para protegerlas, se usa el comando:
    
    ```
    Oficina1# configure terminal
    Oficina1(config)# line vty 0 15
    Oficina1(config-line)# password o1f2i3
    Oficina1(config-line)# login
    Oficina1(config-line)# end
    Oficina1#
    ```
    
    Con esto, cualquier intento de conexión remota (Telnet/SSH) pedirá una contraseña antes de dar acceso al dispositivo.
  
  - **Encriptación**
    
    En Cisco IOS, los archivos startup-config y running-config guardan las contraseñas en texto plano. Esto es un riesgo porque cualquiera que vea esos archivos puede descubrirlas fácilmente.
    
    Para protergerlas, usa el comando:
    
    ```
    Oficina1# configure terminalOficina1(config)# service password-encryptionOficina1(config)#
    ```
    
    Este comando aplica un cifrado básico a todas las contraseñas que estaban sin encriptar, las cuales son de los archivos de configuración, **no** las protege mientras viajan por la red. Su principal función es ocultar contraseñas a simple vista y evitar que usuarios no autorizados las lean.
    
    Finalmente se usa *running-config* para verificar que las contraseñas estén ahora encriptadas.
    
    **Ejemplo de lo que se veria**
    
    ```
    Oficina1(config)# endOficina1# show running-config
    !
    (Output omitted)
    !
    line con 0
    password 7 094F471A1A0A
    login
    !
    line vty 0 4
    password 7 094F471A1A0A
    login
    line vty 5 15
    password 7 094F471A1A0A
    login
    !
    !
    end
    ```



- **Mensaje de aviso**
  
  El banner MOTD en los dispositivos Cisco sirve para mostrar un aviso legal que indica que solo personal autorizado puede acceder al equipo. Aunque las contraseñas protegen, el aviso es importante porque en caso de un ingreso no autorizado puede tener validez legal.
  
  ```
  Oficina1# configure terminal
  Oficina1(config)# banner motd #Solo acceso autorizado#
  ```

---

### Guardar las configuraciones

En un switch Cisco existen dos archivos de configuración:

- **Startup-config**: Guardado en **NVRAM**, contiene los comandos que el dispositivo carga al iniciar o reiniciar. No se borra al apagar.

- **Running-config**: Guardado en **RAM**, refleja la configuración actual aplicada al dispositivo de inmediato. Se pierde al apagar o reiniciar.

Se ejecuta de la siguiente forma: 

*<u>Switch#show running-config</u>* y *<u>Switch#show startup-config</u>*

Para guardar los cambios de la configuración en ejecución en la de inicio, usa: 

*<u>Switch#copy running-config startup-config</u>*

Y si, despues de guardar, siguió configurando, pero no le gusto esa configuración y quiere volver al anterior/ultimo punto de guardado, usa:

*<u>Switch#copy startup-config running-config</u>*



Si los cambios en running-config no sirven y no se han guardado, se pueden eliminar manualmente o reiniciar con *<u>Switch#reload</u>* para volver a la configuración guardada en startup-config.

Si los cambios ya se guardaron en startup-confi, es necesario borrar la configuración con *Switch#erase startup-config*</u> y reiniciar *<u>Switch#reload</u>* para que el switch arranque con la configuración de fábrica.

---

### Puertos y direcciones

Para que los dispositivos finales puedan comunicarse entre sí dentro de una red es necesario que cada uno tenga asignada una dirección IP válida y que además estén correctamente conectados.

Las direcciones IPv4 se escriben en notación decimal punteada, compuesta por cuatro números que van de 0 a 255. Junto con la dirección IP también se requiere una máscara de subred, la cual tiene 32 bits y cumple la función de diferenciar la parte de la dirección que corresponde a la red y la que corresponde al host. Además, los dispositivos utilizan una dirección de gateway predeterminado, que normalmente es la dirección IP del router encargado de permitir la conexión hacia redes externas, incluyendo Internet.

<img src="https://www.netacad.com/content/itn/1.0/courses/content/m2/es-XL/assets/2.6.1-image-1.jpg" title="" alt="" data-align="center">

Las direcciones IPv6 tienen 128 bits y se representan con 32 dígitos hexadecimales agrupados de cuatro en cuatro, separados por dos puntos. No hacen distinción entre mayúsculas y minúsculas.

<img title="" src="https://www.netacad.com/content/itn/1.0/courses/content/m2/es-XL/assets/2.6.1-image-3.png" alt="" data-align="center">

Las redes funcionan gracias a las interfaces de los dispositivos y a los medios que los conectan, cada medio tiene ventajas y desventajas las cuales, generalmente, son: 

- La distancia a través de la cual los medios pueden transportar una señal correctamente.

- El ambiente en el cual se instalará el medio.

- La cantidad de datos y la velocidad a la que se deben transmitir.

- El costo de los medios y de la instalación.

En la mayoría de las redes locales se usa Ethernet, que conecta computadoras, switches y otros equipos mediante cables. Los switches de capa 2 no trabajan directamente con direcciones IP, ya que solo se encargan de conectar dispositivos dentro de la misma red. Sin embargo, para poder administrarlos de forma remota se les asigna una interfaz virtual llamada SVI (por defecto es la VLAN1). Esa dirección IP no es para que el switch funcione como tal, sino únicamente para poder configurarlo a distancia.

---

### Configurar direccionamiento IP

Los dispositivos de red necesitan una dirección IP para comunicarse, al igual que un teléfono necesita un número para llamar. Esta dirección se puede asignar de dos formas:

- **Manual:** configurándola directamente en el dispositivo.

- **Automática:** usando DHCP.

En Windows, la configuración manual se realiza desde:  

`Panel de control > Centro de redes > Cambiar configuración del adaptador > Propiedades del adaptador > Propiedades de Conexión de área local`.

<img src="https://www.netacad.com/content/itn/1.0/courses/content/m2/es-XL/assets/2.7.1-image-1.png" title="" alt="" data-align="center">

Para configurar una dirección manual en Windows, se debe seleccionar Protocolo de Internet versión 4 (TCP/IPv4) en las propiedades del adaptador y abrir sus propiedades. Allí se ingresan la dirección IPv4, la máscara de subred y el gateway predeterminado.

La configuración de IPv6 es similar al procedimiento de IPv4.

<img src="https://www.netacad.com/content/itn/1.0/courses/content/m2/es-XL/assets/2.7.1-image-3.jpg" title="" alt="" data-align="center">

La dirección del servidor DNS es la dirección IPv4 del servidor del sistema de nombres de dominio (DNS), que se utiliza para traducir direcciones IP a direcciones web.



Los dispositivos finales suelen usar DHCP por defecto para obtener su dirección IPv4 de forma automática. DHCP ahorra tiempo y evita errores al asignar automáticamente IP, máscara, gateway y DNS, en lugar de configurarlos manualmente en cada dispositivo.

En Windows, basta con seleccionar:

- *Obtain an IP address automatically*

- *Obtain DNS server address automatically*

Así, la PC obtiene los parámetros de un servidor DHCP.

En IPv6 se emplean DHCPv6 y SLAAC para la configuración automática de direcciones.

<img src="https://www.netacad.com/content/itn/1.0/courses/content/m2/es-XL/assets/2.7.2-image-1.jpg" title="" alt="" data-align="center">

En Windows se puede verificar la configuración IP usando el comando: `ipconfig`

Este comando muestra la dirección IPv4, la máscara de subred y el gateway predeterminado asignados, ya sea de forma manual o a través de DHCP.    

Para acceder a un switch de forma remota, se configura una SVI (interfaz virtual de switch), generalmente en la VLAN 1.

1. Entrar al modo de configuración de la interfaz.

2. Asignar dirección IPv4 y máscara

3. Activar la interfaz.

Con esto, el switch queda listo para comunicarse en la red mediante IPv4.

```
Oficina1# configure terminal
Oficina1(config)# interface vlan 1
Oficina1(config-if)# ip address 192.168.1.20 255.255.255.0
Oficina1(config-if)# no shutdown
Oficina1(config-if)# exit
Oficina1(config)# ip default-gateway 192.168.1.
```



- **Comandos esenciales para la conectividad entre IPs paso a paso**
  
  - **Elementos:**
    
    - PC1
    
    - PC2
    
    - S1(Switch)
    
    - S2(Switch)
  
  - El PC1 esta conectado el S1, el S1 al S2, y el S2 al PC2.
  
  **Configuración del S1**
  
  ```
  Switch>enable
  Switch#configure terminal
  Switch(config)#hostname S1
  S1(config)#line console 0
  S1(config-line)#password cisco
  S1(config-line)#login
  S1(config-line)#exit
  S1(config)#enable secret class
  S1(config)#banner motd #Acceso autorizado únicamente. Los infractores se procesarán en la medida en que lo permita la ley.#
  S1(config)#end
  S1#copy running-config startup-config
  ```
  
  **Configuración del S2**
  
  ```
  Switch>enable
  Switch#configure terminal
  Switch(config)#hostname S2
  S2(config)#line console 0
  S2(config-line)#password cisco
  S2(config-line)#login
  S2(config-line)#exit
  S2(config)#enable secret class
  S2(config)#banner motd #Acceso autorizado únicamente. Los infractores se procesarán en la medida en que lo permita la ley.#
  S2(config)#end
  S2#copy running-config startup-config
  ```
  
  **IP para PC1**
  
  Dirección IP: `192.168.1.1`
  
  Máscara: `255.255.255.0`
  
  **IP para PC2**
  
  Dirección IP: `192.168.1.2`
  
  Máscara: `255.255.255.0`

En el Escritorio de PC1 o PC2, ir a **Command Prompt** y ejecutar el comando *ping 192.168.1.253* para probar la conectividad.



**Configuración de la interfaz de administración en S1**

```
S1>enable
S1#configure terminal
S1(config)#interface vlan 1
S1(config-if)#ip address 192.168.1.253 255.255.255.0
S1(config-if)#no shutdown
S1(config-if)#exit
S1(config)#end
S1#copy running-config startup-config
S1#show ip interface brief
```

*En la parte inferior, o sea, al final despues de usar el ultimo comando, se tendra que ver el vlan1 con la IP (192.168.1.253) en UP*

**Configuración de la interfaz de administración en S2**

```
S2>enable
S2#configure terminal
S2(config)#interface vlan 1
S2(config-if)#ip address 192.168.1.254 255.255.255.0
S2(config-if)#no shutdown
S2(config-if)#exit
S2(config)#end
S2#copy running-config startup-config
```

*En la parte inferior, o sea, al final despues de usar el ultimo comando, se tendra que ver el vlan1 con la IP (192.168.1.254) en UP*



Finalmente se hace la prueba de conectividad diriguiendo a el **Command Prompt** del PC1 o el PC2 y se ejecuta el ping de cada uno de los 3 dispostivos:

- *<u>ping 192.168.1.1</u>* (en este caso se estaria haciendo desde el PC2)

- *<u>ping 192.168.1.253</u>*

- *<u>ping 192.168.1.254</u>*

El mensaje que deberia aparecer seria este:

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-25-02-49-30-image.png)

El porcentaje que esta en Lost = 1 (75% loss), indica el porcentaje de fallo que tiene la conectividad, lo cual se arregla con cada ping que se haga.

---

### Verificar conectividad

En el tema anterior se configuró el direccionamiento IP en switches y PCs, y se verificó la conectividad. Ahora, el objetivo es aprender a verificar interfaces y direcciones en switches y routers mediante la CLI.

- Así como en una PC se usa `ipconfig` para revisar la red, en switches y routers se utilizan comandos específicos.

- El comando `show ip interface brief` permite comprobar el estado de las interfaces y su configuración IP.

- Esta verificación asegura que los dispositivos estén correctamente configurados y funcionando.

- La práctica se realiza en Packet Tracer, usando el mismo archivo del video, aplicando `ipconfig` y `show ip interface brief`.

En la segunda actividad se prueba la conectividad de extremo a extremo, donde el comando `ping` se utiliza para probar la conectividad entre dispositivos de la red o con sitios en Internet.

- Permite verificar si un switch, PC u otro destino responde correctamente.

- Es una herramienta básica de diagnóstico para confirmar que la comunicación funciona.

- En Packet Tracer, se practica descargando el mismo archivo del video y ejecutando pruebas con el comando `ping`.
