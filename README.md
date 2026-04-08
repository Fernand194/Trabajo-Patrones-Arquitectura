# Trabajo Colaborativo: Patrones de Diseño y Arquitectura 🚀

Este proyecto presenta una implementación práctica de dos patrones fundamentales en la arquitectura de software: **Publish-Subscribe** e **Inyección de Dependencia**. El objetivo es demostrar cómo estos patrones ayudan a crear sistemas desacoplados, escalables y fáciles de mantener.

## 👥 Integrantes
* María Fernanda Suárez Neuto

---

## 🛠️ Patrones Implementados

### 1. Publish-Subscribe (Pub/Sub)
Se implementó un sistema de **monitoreo de temperatura**. 
* **Funcionamiento:** Un `EventBroker` actúa como intermediario. El sensor (Publisher) emite datos climáticos sin conocer a sus receptores.
* **Componentes:** Dashboard de visualización y Sistema de Alarma (Subscribers).
* **Ubicación:** `pub_sub_ejemplo.py`

### 2. Inyección de Dependencia (DI)
Se diseñó un **sistema de notificaciones** que cumple con el principio de inversión de dependencia.
* **Funcionamiento:** La clase `Notificador` no crea sus propios servicios de envío. En su lugar, recibe una interfaz de `ServicioMensajeria`.
* **Ventaja:** Permite intercambiar entre enviar un **Email** o un **SMS** sin modificar la lógica principal de la aplicación.
* **Ubicación:** `inyeccion_dependencia.py`

---

## 🚀 Instrucciones de Ejecución

Sigue estos pasos para ejecutar el proyecto localmente:

### Requisitos Previos
* Tener instalado [Python 3.x](https://www.python.org/downloads/)
* Tener instalado [Git](https://git-scm.com/)

### Instalación
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)