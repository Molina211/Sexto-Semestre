# Conceptos de AWS y sus servicios

---

| Capa     | Tú Gestionas                                 | El Proveedor Gestiona            | Analogía                                                                         |
| -------- | -------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------- |
| **SaaS** | **Tus datos y configuración**                | **Todo lo demás**                | **Alquilar una casa amueblada** - Solo usas el espacio                           |
| **PaaS** | **Tus aplicaciones y datos**                 | **Plataforma y infraestructura** | **Alquilar un apartamento** - Traes tus muebles pero el edificio está gestionado |
| **IaaS** | **Sistemas operativos, aplicaciones, datos** | **Hardware virtualizado**        | **Alquilar un terreno** - Construyes tu propia casa                              |

## IaaS (Infrastructure as a Service)

**¿Qué es?**

Infraestructura como Servicio - Alquilas infraestructura informática fundamental.

**Qué gestiona el proveedor:**

- Servidores físicos

- Virtualización

- Almacenamiento

- Redes

- Centros de datos

**Qué gestionas tú:**

- Sistemas operativos

- Aplicaciones

- Middleware

- Runtime

- Datos

**Ejemplos:**

- **AWS EC2** (máquinas virtuales)

- **Google Compute Engine**

- **Microsoft Azure Virtual Machines**

- **DigitalOcean Droplets**

**Casos de uso:**

- Migración de data centers tradicionales

- Entornos de desarrollo y testing

- Almacenamiento y backup

- Hosting de aplicaciones personalizadas

## PaaS (Platform as a Service)

**¿Qué es?**

Plataforma como Servicio - Obtienes una plataforma para desarrollar y desplegar aplicaciones.

**Qué gestiona el proveedor:**

- Infraestructura (IaaS) +

- Sistemas operativos

- Middleware

- Runtime

- Herramientas de desarrollo

**Qué gestionas tú:**

- Tus aplicaciones

- Tus datos

- Configuración de la aplicación

**Ejemplos:**

- **Google App Engine**

- **Heroku**

- **AWS Elastic Beanstalk**

- **Microsoft Azure App Service**

**Casos de uso:**

- Desarrollo ágil de aplicaciones

- CI/CD (Integración Continua/Despliegue Continuo)

- APIs y microservicios

- Desarrollo colaborativo

## SaaS (Software as a Service)

**¿Qué es?**

Software como Servicio - Usas aplicaciones completas a través de internet.

**Qué gestiona el proveedor:**

- **Todo**: Infraestructura, plataforma, aplicación

- Mantenimiento

- Actualizaciones

- Seguridad

- Soporte

**Qué gestionas tú:**

- Tus datos

- Configuración de usuario

- Permisos de acceso

**Ejemplos:**

- **Google Workspace** (Gmail, Drive)

- **Microsoft 365**

- **Salesforce**

- **Slack**

- **Dropbox**

**Casos de uso:**

- Aplicaciones empresariales estándar

- Colaboración y productividad

- CRM y ERP

- Comunicación empresarial
