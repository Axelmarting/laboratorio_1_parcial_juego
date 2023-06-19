import pygame

class Nombre:
    visible = False
    posicion_foto = (0,0)
    posicion_finalizar = (630,600)
    foto_boton_finalizar = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\botonFinalizar.png")
    rectangulo_finalizar = foto_boton_finalizar.get_rect(topleft=posicion_finalizar)
    color_gris = (179, 179, 179) 

    def dibujar(self,pantalla,font_input,ingreso,rectangulo_ingreso):
        if self.visible:
            foto = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\menu_nombre.png")
            pantalla.blit(foto,self.posicion_foto)
            pantalla.blit(self.foto_boton_finalizar,self.posicion_finalizar)
                #DIBUJO TEXTO
            pygame.draw.rect(pantalla,self.color_gris,rectangulo_ingreso,2)
            font_input_surface = font_input.render(ingreso,True,self.color_gris)
            pantalla.blit(font_input_surface,(rectangulo_ingreso.x+5, rectangulo_ingreso.y+5))