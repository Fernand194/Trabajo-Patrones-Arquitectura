import requests
from pub_sub_broker import EventBroker, pantalla_dashboard, sistema_alarma

def enviar_a_microservicio_notif(temp):
    """Esta función actúa como el puente entre microservicios."""
    url = "http://127.0.0.1:5001/notificar"
    data = {"mensaje": f"Alerta de temperatura crítica: {temp}°C"}
    try:
        requests.post(url, json=data)
        print("[MONITOREO] Evento enviado al Microservicio de Notificaciones.")
    except:
        print("[ERROR] No se pudo contactar al Microservicio de Notificaciones.")

# Configuración Pub/Sub
bus = EventBroker()
bus.suscribir("alerta_clima", enviar_a_microservicio_notif)

if __name__ == "__main__":
    print("--- Simulando Sensor de Clima ---")
    temp_actual = 38
    if temp_actual > 30:
        bus.publicar("alerta_clima", temp_actual)