from constantes import velocidad_objetos, alto_ventana
from funciones import generar_posicion_random, actualizar_posicion_rect

class MotoRival:

    def __init__(self, posicion, foto) -> None:
        self.posicion = posicion
        self.foto = foto
        self.rectangulo = self.foto.get_rect()

    def mover(self):
        if self.posicion[1] < alto_ventana:
            self.posicion[1] += velocidad_objetos  # se desplaza 10 pixeles hacia abajo
        else:
            self.posicion[1] = -420  # reinicia la posición en la parte superior
            self.posicion[0] = generar_posicion_random()  # genera una nueva posición aleatoria en el eje x

        actualizar_posicion_rect(self)

    def dibujar(self,pantalla):
        pantalla.blit(self.foto,(self.posicion))
