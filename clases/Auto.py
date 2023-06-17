import pygame
from constantes import limites_pantalla
from funciones import actualizar_posicion_rect

class Auto:
    foto = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\auto_verde-removebg-preview.png")
    foto = pygame.transform.scale(foto,(100,170))
    posicion = [330,500]
    velocidad_actual = 10
    rectangulo = foto.get_rect()
    vidas = 3
    colisionando = False

    def mover(self):
        velocidad_min = 10
        velocidad_max = 40

        lista_teclas = pygame.key.get_pressed()  #este evento nunca va dentro del for.
        #si tengo una tecla presionada:
        if True in lista_teclas:
            if lista_teclas[pygame.K_RIGHT]:
                if self.posicion[0] < limites_pantalla[0]: #limite derecho
                    self.posicion[0] += self.velocidad_actual
            if lista_teclas[pygame.K_LEFT]:
                if self.posicion[0] > limites_pantalla[1]: #limite izquierdo
                    self.posicion[0] -= self.velocidad_actual
            if lista_teclas[pygame.K_UP]:
                if self.posicion[1] > limites_pantalla[2]: #limite superior
                    self.posicion[1] -= self.velocidad_actual
            if lista_teclas[pygame.K_DOWN]:
                if self.posicion[1] < limites_pantalla[3]: #limite inferior
                    self.posicion[1] += self.velocidad_actual
            if lista_teclas[pygame.K_1]:
                    self.velocidad_actual = velocidad_min
            if lista_teclas[pygame.K_2]:
                    self.velocidad_actual = velocidad_max
        
        actualizar_posicion_rect(self)

    def reiniciar(self):
        self.posicion = [330, 500]  # Establecer la posición inicial
        self.velocidad_actual = 10  # Restablecer la velocidad
        # self.rectangulo = self.foto.get_rect()  # Restablecer el rectángulo de colisión

    def dibujar(self,pantalla):
        pantalla.blit(self.foto,(self.posicion))