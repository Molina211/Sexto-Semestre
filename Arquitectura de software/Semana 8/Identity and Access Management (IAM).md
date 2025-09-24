# Identity and Access Management (IAM)

---

## 1. ¿Qué es IAM?

**IAM (Identity and Access Management)** o **Gestión de Identidad y Acceso** es un marco de políticas y tecnologías fundamental en la arquitectura de software que asegura que **las personas o sistemas adecuados (Identidades) tengan el acceso correcto (Permisos) a los recursos tecnológicos adecuados, en el momento preciso.**

En esencia, es el portero de seguridad digital que responde a tres preguntas clave:

- **¿Quién eres?** (Autenticación)

- **¿Qué tienes permiso para hacer?** (Autorización)

- **¿A qué recursos puedes acceder?** (Control de Acceso)

## 2. ¿Por qué es Importante?

La importancia de IAM es crítica en la arquitectura moderna por varias razones:

- **Seguridad:** Es la primera línea de defensa. Previene brechas de datos al evitar accesos no autorizados.

- **Cumplimiento Normativo:** Ayuda a cumplir con regulaciones como GDPR, HIPAA, PCI-DSS, que exigen un control estricto sobre quién accede a la información sensible.

- **Productividad:** Permite a los usuarios acceder rápidamente a las herramientas que necesitan para trabajar (Single Sign-On), sin múltiples contraseñas.

- **Escalabilidad y Gestión Eficiente:** En entornos con miles de usuarios y servicios (como la nube), gestionar permisos manualmente es imposible. IAM automatiza este proceso.

- **Experiencia del Usuario (UX):** Proporciona un acceso seguro pero sin fricciones.

- **Principio de Mínimo Privilegio:** Aplica esta best practice de seguridad, concediendo a los usuarios solo los permisos absolutamente necesarios para realizar su trabajo.

## 3. Funciones Principales

Un sistema IAM se compone de cuatro funciones centrales:

| Función                               | Descripción                                                                                                                                                                                              |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Autenticación (Authentication)** | Verificar la identidad de un usuario, sistema o servicio. Responde a "¿Eres quien dices ser?". Ejemplos: contraseñas, MFA (Autenticación Multifactor), huellas dactilares, certificados digitales.       |
| **2. Autorización (Authorization)**   | Determinar qué permisos tiene una identidad autenticada. Responde a "¿Qué te está permitido hacer?". Define las acciones (leer, escribir, eliminar) sobre los recursos (archivos, bases de datos, APIs). |
| **3. Gestión de Usuarios**            | Gestionar el ciclo de vida completo de las identidades: creación (onboarding), actualización de permisos (change of role) y eliminación (offboarding) de cuentas.                                        |
| **4. Auditoría y Reportes**           | Registrar y monitorizar toda la actividad relacionada con el acceso (logs de inicio de sesión, intentos fallidos, cambios de permisos). Es crucial para la forense digital y el cumplimiento normativo.  |

## 4. Roles de IAM (Ejemplos Comunes)

Los "roles" son una forma de agrupar permisos y asignarlos a una identidad de manera conjunta. Son fundamentales en la nube (AWS, Azure, GCP).

- **Administrador/Superusuario:** Acceso total a todos los recursos y configuraciones del sistema.

- **Usuario Final/Empleado:** Permisos básicos para usar aplicaciones específicas necesarias para su trabajo (ej: suite de Office, CRM).

- **Desarrollador:** Acceso a entornos de desarrollo, repositorios de código y herramientas de CI/CD, pero no a producción.

- **Auditor/Visualizador de Solo Lectura:** Puede ver configuraciones y logs, pero no puede realizar cambios.

- **Rol de Servicio/Máquina:** Usado por aplicaciones o servicios (no por personas) para interactuar con otros servicios de forma segura. Ej: una aplicación web que necesita leer de una base de datos.

## 5. Modelos de Control de Acceso

Son los modelos lógicos que definen **cómo** se conceden los permisos.

| Modelo                                    | Descripción                                                                                                                                                                                 | Ejemplo                                                                                                                                                                                                                                                 |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DAC (Discretionary Access Control)**    | El propietario del recurso decide quién tiene acceso. Es flexible pero menos seguro.                                                                                                        | Permisos de archivos en un sistema Unix/Windows.                                                                                                                                                                                                        |
| **MAC (Mandatory Access Control)**        | El acceso se define por políticas centrales basadas en etiquetas de seguridad (ej: "Confidencial", "Secreto"). El usuario no puede modificarlo. Muy seguro, usado en gobiernos y militares. | Un sistema donde un usuario con nivel "Confidencial" no puede acceder a un documento etiquetado como "Secreto".                                                                                                                                         |
| **RBAC (Role-Based Access Control)**      | **El más común en empresas.** Los permisos se asignan a roles (ej: "Vendedor", "Gerente"), y los usuarios se asignan a uno o más roles.                                                     | Todos los usuarios con el rol "Contador" tienen acceso al software de contabilidad.                                                                                                                                                                     |
| **ABAC (Attribute-Based Access Control)** | Modelo avanzado y granular. El acceso se concede basándose en atributos del usuario, el recurso, la acción y el contexto.                                                                   | "Permitir acceso al documento si el usuario es del **departamento de Finanzas** (atributo del usuario) Y el documento tiene la etiqueta **"Presupuesto"** (atributo del recurso) Y la conexión es desde la **red corporativa** (atributo de contexto)". |

## 6. Ejemplo Práctico: Una Aplicación Bancaria

Imagina una aplicación móvil de un banco.

1. **Autenticación:**
   
   - El usuario introduce su número de cliente y contraseña. Luego, el sistema solicita un código de un solo uso enviado a su teléfono (MFA).

2. **Gestión de Usuarios:**
   
   - Cuando un nuevo cliente se registra, el sistema IAM crea una identidad para él en la base de datos.

3. **Autorización (usando RBAC):**
   
   - **Rol: "Cliente Standard"**: Puede ver sus cuentas, realizar transferencias a sus propias cuentas y pagar servicios.
   
   - **Rol: "Cliente Premium"**: Tiene los permisos de "Cliente Standard" **más** la capacidad de solicitar préstamos y realizar inversiones.
   
   - **Rol: "Empleado de Soporte"**: Puede ver información limitada de clientes para asistirlos, pero **no** puede realizar transacciones por ellos.

4. **Control de Acceso (en acción):**
   
   - Un usuario autenticado con el rol "Cliente Standard" intenta acceder a la pantalla de "Solicitar Préstamo". El sistema IAM verifica sus permisos y **niega el acceso** porque su rol no lo incluye.

5. **Auditoría:**
   
   - El sistema registra cada inicio de sesión, cada transferencia realizada y cada intento de acceso denegado. Si hay una actividad sospechosa (muchos intentos fallidos), se alerta al equipo de seguridad.


