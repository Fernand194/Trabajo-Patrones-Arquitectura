from abc import ABC, abstractmethod

# Este es el PUERTO (Interface)
class PuertoNotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass