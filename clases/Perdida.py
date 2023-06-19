import pygame

class Perdida:
    posicion = 0,0
    visible = False
    posicion_abandonar = (650,400)
    posicion_reintentar = (130,400)
    foto_boton_abandonar = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\botonAbandonar.png")
    rectangulo_abandonar = foto_boton_abandonar.get_rect(topleft=posicion_abandonar)
    foto_boton_reintentar = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\botonReintentar.png")
    rectangulo_reintentar = foto_boton_reintentar.get_rect(topleft=posicion_reintentar)

    def dibujar(self, pantalla):
        if self.visible:
            foto_pausa = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\menu_perdida.png")
            pantalla.blit(foto_pausa, (self.posicion))
            pantalla.blit(self.foto_boton_abandonar, self.posicion_abandonar)
            pantalla.blit(self.foto_boton_reintentar, self.posicion_reintentar)