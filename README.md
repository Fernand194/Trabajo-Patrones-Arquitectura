# Trabajo Colaborativo: Arquitectura de Microservicios y Patrones de Diseño

Este proyecto demuestra la implementación de una arquitectura moderna y desacoplada, utilizando **Microservicios**, **Arquitectura Hexagonal**, y patrones como **Publish-Subscribe** e **Inyección de Dependencia**.

## Integrantes
* María Fernanda Suárez Neuto

---

## Arquitectura del Sistema

El sistema se ha dividido en dos microservicios independientes que se comunican mediante una **API REST**:

### 1. Microservicio de Monitoreo (`servicio-monitoreo`)
* **Responsabilidad:** Monitorea variables climáticas (simuladas).
* **Patrón Publish-Subscribe:** Utiliza un `EventBroker` interno para gestionar eventos. Cuando se detecta una temperatura crítica, el broker dispara una acción que notifica al siguiente microservicio.
* **Tecnología:** Python + Requests.

### 2. Microservicio de Notificaciones (`servicio-notificaciones`)
* **Responsabilidad:** Gestionar el envío de alertas a través de diferentes medios.
* **Arquitectura Hexagonal (Ports & Adapters):** * **Dominio:** Define la interfaz (Puerto) `PuertoNotificacion`.
    * **Aplicación:** Contiene el caso de uso `CasoDeUsoNotificar`, el cual es independiente de la tecnología de envío.
    * **Infraestructura:** Contiene los Adaptadores (`AdaptadorEmail`, `AdaptadorSMS`) que implementan la lógica técnica.
* **Inyección de Dependencia:** Las dependencias de infraestructura se inyectan en el caso de uso en tiempo de ejecución.
* **Tecnología:** Python + Flask.

---

## Requisitos e Instalación

### Pre-requisitos
* Python 3.10+
* Librerías necesarias:
  ```bash
  pip install flask requests