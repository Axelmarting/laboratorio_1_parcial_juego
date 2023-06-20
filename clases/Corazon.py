import pygame

class Corazon:
    def __init__(self, posicion) -> None:
        self.posicion_corazon = posicion
        self.visible = True

    def dibujar(self, pantalla):
        if self.visible:
            foto_corazon = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\ordenado\fotos\corazon.png")
            foto_corazon = pygame.transform.scale(foto_corazon,(50,50))
            pantalla.blit(foto_corazon, self.posicion_corazon)
    
    def eliminar(self):
        self.visible = False

    def reaparecer(self):
        self.visible = True