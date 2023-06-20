import pygame

class Scores:
    visible = False
    posicion_foto = (0,0)
    posicion_finalizar = (630,600)
    foto_boton_finalizar = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\botonFinalizar.png")
    rectangulo_finalizar = foto_boton_finalizar.get_rect(topleft=posicion_finalizar)
    color_gris = (179, 179, 179) 

    def dibujar(self,pantalla,lista_ordenada, font_input):
        if self.visible:
            foto = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\menu_scores.png")
            pantalla.blit(foto,self.posicion_foto)
            pantalla.blit(self.foto_boton_finalizar,self.posicion_finalizar)

            for i, score in enumerate(lista_ordenada[:3]):
                nombre = score["nombre"]
                tiempo = score["tiempo"]
                texto_score = font_input.render("{0}. {1}: {2}s".format(i+1,nombre,tiempo), True, self.color_gris)

                if i == 0:
                    posicion = (300,250)
                elif i == 1:
                    posicion = (300,350)
                elif i == 2:
                    posicion = (300,450)

                pantalla.blit(texto_score, posicion)


            
