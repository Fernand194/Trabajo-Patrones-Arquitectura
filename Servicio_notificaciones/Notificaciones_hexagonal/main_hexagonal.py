from flask import Flask, request, jsonify
from infraestructura import AdaptadorEmail
from aplicacion import CasoDeUsoNotificar

app = Flask(__name__)

@app.route('/notificar', methods=['POST'])
def recibir_alerta():
    datos = request.json
    mensaje = datos.get("mensaje")
    
    # Aplicamos Arquitectura Hexagonal e Inyección
    herramienta = AdaptadorEmail()
    caso_uso = CasoDeUsoNotificar(herramienta)
    caso_uso.ejecutar(mensaje)
    
    return jsonify({"status": "Notificación procesada"}), 200

if __name__ == "__main__":
    # Este servicio corre en el puerto 5001
    app.run(port=5001)