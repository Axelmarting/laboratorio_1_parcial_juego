import pygame
from constantes import velocidad_objetos,alto_ventana
from funciones import generar_posicion_random, actualizar_posicion_rect

class Aceite:
    foto = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\mancha_aceite.png")
    foto = pygame.transform.scale(foto,(70,70))
    posicion = [430,-170]
    rectangulo = foto.get_rect()

    def mover(self):
        if self.posicion[1] < alto_ventana:
            self.posicion[1] += velocidad_objetos  # se desplaza 10 pixeles hacia abajo
        else:
            self.posicion[1] = -100  # reinicia la posición en la parte superior
            self.posicion[0] = generar_posicion_random()
        
        actualizar_posicion_rect(self)

    def dibujar(self, pantalla):
        pantalla.blit(self.foto,(self.posicion))