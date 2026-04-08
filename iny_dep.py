# =================================================================
# PATRÓN DE DISEÑO: INYECCIÓN DE DEPENDENCIA (DI)
# El objetivo es que la clase de alto nivel no cree sus dependencias,
# sino que las reciba (sean "inyectadas").
# =================================================================

from abc import ABC, abstractmethod

# 1. Definimos una Interfaz (Contrato)
class ServicioMensajeria(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

# 2. Implementaciones concretas (Las herramientas)
class ServicioEmail(ServicioMensajeria):
    def enviar(self, mensaje):
        print(f"[EMAIL] Enviando correo electrónico: {mensaje}")

class ServicioSMS(ServicioMensajeria):
    def enviar(self, mensaje):
        print(f"[SMS] Enviando mensaje de texto: {mensaje}")

# 3. La clase que recibe la inyección
class Notificador:
    def __init__(self, servicio: ServicioMensajeria):
        # Aquí ocurre la magia: Inyectamos la dependencia por el constructor
        self.servicio = servicio

    def enviar_alerta(self, texto):
        self.servicio.enviar(texto)

# --- Función para ejecutar el ejemplo ---
def ejecutar_di():
    print("--- Ejemplo con Inyección de Email ---")
    email_service = ServicioEmail()
    # Inyectamos el servicio de Email
    app_con_email = Notificador(email_service)
    app_con_email.enviar_alerta("¡Tu código ha sido subido a GitHub!")

    print("\n--- Ejemplo con Inyección de SMS ---")
    sms_service = ServicioSMS()
    # Inyectamos el servicio de SMS sin cambiar ni una línea de la clase Notificador
    app_con_sms = Notificador(sms_service)
    app_con_sms.enviar_alerta("¡Alerta de seguridad en tu cuenta!")

if __name__ == "__main__":
    ejecutar_di()