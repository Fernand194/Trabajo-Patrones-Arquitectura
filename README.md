# 🚀 Sistema de Monitoreo Ambiental - Arquitectura de Microservicios

Este proyecto es una implementación avanzada de un sistema de alertas climáticas industriales. Demuestra el uso de **Microservicios**, **Arquitectura Hexagonal**, y patrones de diseño como **Publish-Subscribe** e **Inyección de Dependencia**.

---

## 📝 1. Descripción del Caso de Uso

**Contexto:** En entornos críticos como centros de datos, el monitoreo de temperatura es vital para prevenir fallos de hardware.
**Problema:** Un sistema monolítico donde el sensor depende directamente del servicio de correo es rígido y difícil de mantener. Si falla el proveedor de email, el sensor deja de funcionar.
**Solución:** Se diseñó un sistema desacoplado donde un sensor publica eventos y un microservicio independiente procesa las notificaciones aplicando principios de arquitectura limpia.

---

## 🏗️ 2. Arquitectura y Patrones Aplicados

### A. Enfoque de Microservicios
El sistema se divide en dos unidades independientes que se comunican vía **API REST (HTTP/POST)**:
* **Servicio de Monitoreo:** (Publisher) Captura datos del entorno.
* **Servicio de Notificaciones:** (Subscriber) Gestiona el envío de alertas.

### B. Arquitectura Hexagonal (Ports & Adapters)
Implementada en el servicio de notificaciones para aislar la lógica de negocio de la tecnología:
* **Dominio (`dominio.py`):** Define los "Puertos" (interfaces abstractas).
* **Aplicación (`aplicacion.py`):** Contiene el "Core" o caso de uso, independiente de si el mensaje sale por Email o SMS.
* **Infraestructura (`infraestructura.py`):** Contiene los "Adaptadores" técnicos que interactúan con el mundo exterior.

### C. Patrones de Diseño
* **Publish-Subscribe:** Utilizado en el emisor para desacoplar el sensor de la lógica de red. El sensor publica en un `EventBroker` interno.
* **Inyección de Dependencia (DI):** Se aplican inyecciones por constructor en el archivo principal para pasar adaptadores de infraestructura al núcleo de la aplicación sin que este los conozca.

---

## 🚀 3. Guía de Ejecución Local

### Requisitos Previos
* Python 3.10 o superior.
* Instalación de librerías necesarias:
    ```bash
    pip install flask requests
    ```

### Instrucciones paso a paso
Debido a la naturaleza de los microservicios, se deben abrir **dos terminales separadas** en VS Code:

#### Paso 1: Microservicio de Notificaciones (Receptor)
1. Navega a la carpeta: `cd servicio-notificaciones/Notificaciones_hexagonal`
2. Ejecuta: `python main_hexagonal.py`
3. *El servidor quedará "escuchando" en el puerto 5001.*

#### Paso 2: Microservicio de Monitoreo (Emisor)
1. Abre una **nueva terminal**.
2. Navega a la carpeta: `cd servicio-monitoreo`
3. Ejecuta: `python main_clima.py`
4. *El sensor detectará la temperatura y enviará la alerta automáticamente al primer microservicio.*

---

## 📁 4. Estructura del Proyecto

```text
├── servicio-monitoreo/           # Microservicio A (Publisher)
│   ├── pub_sub_ejemplo.py        # Lógica de patrón Pub/Sub
│   └── main_clima.py             # Emisor de eventos hacia la API
└── servicio-notificaciones/      # Microservicio B (Subscriber + Hexagonal)
    └── Notificaciones_hexagonal/
        ├── dominio.py            # Puerto (Interfaz abstracta)
        ├── infraestructura.py     # Adaptadores (Email / SMS)
        ├── aplicacion.py          # Caso de Uso (Lógica de Negocio)
        └── main_hexagonal.py      # Servidor Flask e Inyección de Dependencia