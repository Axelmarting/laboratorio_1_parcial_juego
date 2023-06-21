from constantes import velocidad_objetos, alto_ventana

class Fondo:
    
    def __init__(self, posicion) -> None:
        self.posicion_fondo = posicion

    def mover(self, posicion_reaparecer):
        if self.posicion_fondo[1] - 1 < alto_ventana:
            self.posicion_fondo[1] = self.posicion_fondo[1] + velocidad_objetos
        else:
            self.posicion_fondo[1] = posicion_reaparecer
    
    def dibujar(self,pantalla,foto_camino):
        pantalla.blit(foto_camino,(self.posicion_fondo))