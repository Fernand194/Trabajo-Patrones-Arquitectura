# =================================================================
# PATRÓN DE ARQUITECTURA: PUBLISH-SUBSCRIBE
# Este patrón desacopla al emisor (Publisher) de los receptores (Subscribers)
# mediante un intermediario llamado Broker.
# =================================================================

class EventBroker:
    """El Broker actúa como intermediario para gestionar las suscripciones."""
    def __init__(self):
        self.subscriptores = {}

    def suscribir(self, evento, callback):
        """Permite que un componente se anote a un tipo de evento."""
        if evento not in self.subscriptores:
            self.subscriptores[evento] = []
        self.subscriptores[evento].append(callback)

    def publicar(self, evento, datos):
        """Notifica a todos los interesados que algo ocurrió."""
        if evento in self.subscriptores:
            for callback in self.subscriptores[evento]:
                callback(datos)

# --- Implementación de los Componentes ---

def pantalla_dashboard(temp):
    print(f"[PANTALLA] Actualizando gráfico: La temperatura es {temp}°C")

def sistema_alarma(temp):
    if temp > 30:
        print(f"[ALARMA] ¡PELIGRO! Temperatura crítica: {temp}°C")

# --- Ejecución del ejemplo ---
if __name__ == "__main__":
    bus_eventos = EventBroker()

    # Los suscriptores se anotan al canal "cambio_clima"
    bus_eventos.suscribir("cambio_clima", pantalla_dashboard)
    bus_eventos.suscribir("cambio_clima", sistema_alarma)

    # El "Publisher" (el sensor) emite datos sin saber quién escucha
    print("--- Emitiendo temperatura normal ---")
    bus_eventos.publicar("cambio_clima", 22)

    print("\n--- Emitiendo temperatura alta ---")
    bus_eventos.publicar("cambio_clima", 35)