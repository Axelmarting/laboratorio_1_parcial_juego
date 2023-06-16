import pygame

class Pausa:
    posicion = 0,0
    visible = False

    def dibujar(self, pantalla):
        if self.visible:
            foto_pausa = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\Menu_pausa.png")
            pantalla.blit(foto_pausa, (self.posicion))
