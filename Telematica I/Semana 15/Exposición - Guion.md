# Objetivos

•Implementar subnetting para seis subredes funcionales.

•Simular y validar la conectividad end-to-end, la resolución DNS y los servicios de red.

•Configurar los servicios críticos en servidores accesibles desde cualquier LAN.

•Diseñar y validar una red de clase empresarial para 590 usuarios.

---

# Análisis de la problemática

## Situación actual:

•Red doméstica sin segmentación ni control de tráfico.

•Un solo dominio de broadcast provocando colisiones y alta latencia.

•Ausencia de servicios centralizados (DHCP, DNS, HTTP, FTP, SMTP).

## Necesidad:

Diseñar una arquitectura modular y escalable que:

•Separe las áreas en 6 LAN independientes.

•Garantice alta disponibilidad y rendimiento.

•Centralice los servicios en la subred de Soporte TI.

•Asegure la conectividad y seguridad entre todos los departamentos.

---

# Diseño de red

**Diseño lógico (direccionamiento y topología):**

- Bloque asignado: **192.168.0.0/21 (2048 hosts)**
    
- Subnetting con prefijo **/24** → 6 LAN + 1 red de servidores.
    
- Asignación de direcciones mediante **VLSM**, optimizada por cantidad de hosts.
    
- **DHCP** propio por subred, con **gateway redundante** en routers principales.
    
- Servidores (DHCP, DNS, HTTP, FTP, SMTP) ubicados en la LAN de Soporte TI.
    

**Diseño físico (infraestructura):**

- **6 Switches Cisco 2960**, uno por LAN.
    
- **1 Router Cisco 1941** (o dos si hay redundancia).
    
- Enlaces troncales entre switches y router para segmentación VLAN.
    
- **Cables UTP Cat6** y tramas simuladas en Packet Tracer.

--- 
## 🧩 **1. ¿Qué equipos de interconexión se deberían utilizar para esta nueva red?**

Para la nueva infraestructura de **GameTech Studios S.A.S.** se requieren **equipos de interconexión de clase empresarial** que garanticen rendimiento, estabilidad y escalabilidad.

**Equipos seleccionados:**

- **Routers Cisco 1941 o superiores:** encargados del **enrutamiento entre subredes (inter-VLAN routing)**, conexión hacia Internet y aplicación de políticas de seguridad y redundancia.
    
- **Switches Cisco Catalyst 2960:** utilizados en cada LAN para la **conmutación de capa 2**, segmentación mediante VLANs, priorización de tráfico y soporte para enlaces troncales hacia el router principal.
    
- **Servidor central de red:** ubicado en la LAN de Soporte TI, aloja los servicios DHCP, DNS, HTTP, FTP y SMTP.
    
- **Medio de transmisión:** cableado estructurado **UTP categoría 6** y conectores RJ-45 para enlaces LAN, con posibilidad de **fibra óptica** en el backbone principal si se requiere mayor velocidad.
    
- **Equipos finales:** estaciones de trabajo, laptops y dispositivos IoT conectados a cada subred.

## ⚙️ **2. ¿Qué es y cómo se implementan los servicios de aplicación señalados?**

Los **servicios de aplicación** garantizan la funcionalidad y la comunicación interna dentro de la red.  
Todos se implementan en el **servidor de la subred de Soporte TI** y son accesibles desde cualquier LAN:

|Servicio|Función|Implementación en Packet Tracer / Red real|
|---|---|---|
|**DHCP (Dynamic Host Configuration Protocol)**|Asigna automáticamente direcciones IP, máscara, gateway y DNS a los dispositivos de cada subred.|Configurado en el servidor con un pool distinto por LAN (/24).|
|**DNS (Domain Name System)**|Traduce nombres de dominio a direcciones IP internas.|Servidor configurado con zona local (ej. gametech.local).|
|**HTTP (HyperText Transfer Protocol)**|Permite alojar aplicaciones web internas o portales de documentación.|Servidor HTTP activo en puerto 80.|
|**FTP (File Transfer Protocol)**|Facilita el intercambio de archivos entre usuarios y servidores.|Servidor con autenticación básica y permisos por carpeta.|
|**SMTP (Simple Mail Transfer Protocol)**|Gestiona el envío de correos internos entre departamentos.|Servidor configurado con buzones locales y dominio corporativo.|

Estos servicios se verifican mediante **pruebas de conectividad y acceso remoto** en cada LAN, garantizando su disponibilidad en toda la red.

## 🌐 **3. ¿Cómo se debe realizar la asignación de direccionamiento?**

La red utiliza un **bloque IP inicial /21** (por ejemplo: `192.168.0.0/21`), equivalente a **2048 direcciones**, que se divide en **seis subredes /24** mediante **subnetting y VLSM (Variable Length Subnet Masking)**.

**Esquema de direccionamiento propuesto:**

|LAN|Departamento|Rango de IP|Máscara|Gateway|Nº de hosts|
|---|---|---|---|---|---|
|1|Desarrollo de Software|192.168.0.0 – 192.168.0.255|/24|192.168.0.1|254|
|2|Diseño 3D y Animación|192.168.1.0 – 192.168.1.255|/24|192.168.1.1|254|
|3|QA y Testing|192.168.2.0 – 192.168.2.255|/24|192.168.2.1|254|
|4|Infraestructura y Soporte TI|192.168.3.0 – 192.168.3.255|/24|192.168.3.1|254|
|5|Marketing y Publicación|192.168.4.0 – 192.168.4.255|/24|192.168.4.1|254|
|6|Administración y RRHH|192.168.5.0 – 192.168.5.255|/24|192.168.5.1|254|

**Direcciones reservadas:**

- Primer IP: **Gateway de la LAN**.
    
- Última IP: **Broadcast**.
    
- IPs iniciales del rango: **servidores y dispositivos críticos**.
    

Este esquema asegura **organización, control de tráfico, escalabilidad y facilidad de administración**, cumpliendo con las mejores prácticas de **Cisco Networking Academy**.

