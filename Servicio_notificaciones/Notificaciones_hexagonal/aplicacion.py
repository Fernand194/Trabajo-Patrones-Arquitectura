from dominio import PuertoNotificacion

class CasoDeUsoNotificar:
    def __init__(self, servicio: PuertoNotificacion):
        # Inyectamos el puerto. La aplicación no sabe si es Email o SMS.
        self.servicio = servicio

    def ejecutar(self, texto: str):
        # Lógica de negocio (ejemplo: agregar un prefijo de seguridad)
        mensaje_final = f"ALERTA DE SISTEMA: {texto}"
        self.servicio.enviar(mensaje_final)