from dominio import PuertoNotificacion

# ADAPTADOR 1: Email
class AdaptadorEmail(PuertoNotificacion):
    def enviar(self, mensaje: str):
        print(f"📧 [INFRAESTRUCTURA] Conectando a servidor SMTP... Enviando Email: {mensaje}")

# ADAPTADOR 2: SMS
class AdaptadorSMS(PuertoNotificacion):
    def enviar(self, mensaje: str):
        print(f"📱 [INFRAESTRUCTURA] Conectando a Gateway GSM... Enviando SMS: {mensaje}")