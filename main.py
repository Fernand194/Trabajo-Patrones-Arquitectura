# --- 1. IMPORTACIONES (Siempre al principio) ---
import sys
# Importamos las clases y funciones de tus otros archivos
from pub_sub import EventBroker, pantalla_dashboard, sistema_alarma
from iny_dep import ejecutar_di

# --- 2. FUNCIONES DE APOYO ---
def ejecutar_logica_pub_sub():
    """Esta función prepara y corre el ejemplo de Pub/Sub."""
    bus = EventBroker()
    # Suscribimos los componentes al evento 'cambio_clima'
    bus.suscribir("cambio_clima", pantalla_dashboard)
    bus.suscribir("cambio_clima", sistema_alarma)
    
    print("Publicando temperatura de 25°C...")
    bus.publicar("cambio_clima", 25)
    print("\nPublicando temperatura de 35°C (Activará alarma)...")
    bus.publicar("cambio_clima", 35)

def mostrar_menu():
    print("\n" + "="*45)
    print("   SISTEMA DE DEMOSTRACIÓN DE PATRONES")
    print("="*45)
    print("1. Ejecutar Patrón Publish-Subscribe")
    print("2. Ejecutar Patrón Inyección de Dependencia")
    print("3. Salir")
    print("-" * 45)

# --- 3. BLOQUE PRINCIPAL ---
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            print("\n--- INICIANDO PUBLISH-SUBSCRIBE ---")
            ejecutar_logica_pub_sub()
            
        elif opcion == "2":
            print("\n--- INICIANDO INYECCIÓN DE DEPENDENCIA ---")
            ejecutar_di()
            
        elif opcion == "3":
            print("Cerrando el programa. ¡Adiós!")
            sys.exit()
        else:
            print("⚠️ Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()