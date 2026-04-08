import sys

# --- IMPORTACIÓN DE PATRONES ---
# (Asumiendo que crearás estos archivos a continuación)
# from src.pub_sub import ejecutar_pub_sub
# from src.di import ejecutar_di

def mostrar_menu():
    print("="*40)
    print(" TRABAJO COLABORATIVO: PATRONES DE DISEÑO")
    print("="*40)
    print("1. Ejecutar Patrón Publish-Subscribe")
    print("2. Ejecutar Patrón Inyección de Dependencia")
    print("3. Salir")
    print("-"*40)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- INICIANDO PUBLISH-SUBSCRIBE ---")
            # Aquí llamaremos a la lógica de Pub/Sub
            print("Ejecutando lógica de eventos...\n")
            
        elif opcion == "2":
            print("\n--- INICIANDO INYECCIÓN DE DEPENDENCIA ---")
            # Aquí llamaremos a la lógica de DI
            print("Inyectando servicios...\n")
            
        elif opcion == "3":
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()