"""
ERRORES:
Los botones de jugar y abandonar se pueden pulsar en cualquier momento del juego.
No me elimina los corazones de las vidas.

Cosas por hacer:
Ingrese nombre
sonidos de colisiones
Programar Score.
Movimientos de autos rivales.
Hacer algo cuando pise el aceite.
pantalla de perdida


Cosas no tan importantes:
seleccionar el auto para jugar
poner temporizador.

"""
import pygame
from constantes import *
from clases.Auto import Auto
from clases.Fondo import Fondo
from clases.MotoRival import MotoRival
from clases.Aceite import Aceite
from clases.Corazon import Corazon
from clases.Pausa import Pausa
from clases.Menu import Menu
from clases.Perdida import Perdida
from funciones import eliminar_corazon

pygame.init()

#TIMER
timer_segundos = pygame.USEREVENT  #Este es un evento que creo yo. No es uno existente.
pygame.time.set_timer(timer_segundos, 100) #1000millis = 1seg
pygame.display.set_caption("AMG cars")

#PANTALLA
pantalla = pygame.display.set_mode((ancho_ventana,alto_ventana))

#CREACION AUTO PRINCIPAL:
auto_principal = Auto()

#CREACION DE FONDOS:
camino_1 = Fondo(posicion_carretera_1)
camino_2 = Fondo(posicion_carretera_2)
camino_3 = Fondo(posicion_carretera_3)

bosque_izq_1 = Fondo(posicion_bosque_izq_1)
bosque_izq_2 = Fondo(posicion_bosque_izq_2)
bosque_izq_3 = Fondo(posicion_bosque_izq_3)

bosque_der_1 = Fondo(posicion_bosque_der_1)
bosque_der_2 = Fondo(posicion_bosque_der_2)
bosque_der_3 = Fondo(posicion_bosque_der_3)

#CREACION MOTOS ENEMIGAS:
moto_enemiga_1 = MotoRival(posicion_moto_1,foto_moto_1)
moto_enemiga_2 = MotoRival(posicion_moto_2,foto_moto_2)

#CREACION ACEITE:
mancha_aceite = Aceite()

#CREACION CORAZON:
corazon_1 = Corazon(posicion_corazon)
corazon_2 = Corazon(posicion_corazon_2)
corazon_3 = Corazon(posicion_corazon_3)

#CREACION PAUSA
menu_pausa = Pausa()

#CREACION MENU PRINCIPAL
menu_principal = Menu()

#CREACION MENU PERDIDA
menu_perdida = Perdida()

#Puede colisionar
"""
Creo esta variable ya que cuando toco jugar automaticamente me borra un corazon, con esto se soluciona
"""
puede_colisionar = False

#reinicio de juego para cuando toque abandonar
reiniciar_juego = False

flag_correr = True
while flag_correr:
    #que traiga todos los eventos y los guarde en una lista.
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        #detectamos la salida.
        if evento.type == pygame.QUIT:
            flag_correr = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if menu_principal.rectangulo_jugar.collidepoint(evento.pos):
                print("CLICK sobre boton jugar")
                menu_principal.visible = False
                menu_pausa.juego_pausado = False
                puede_colisionar = True   
            elif menu_principal.rectangulo_scores.collidepoint(evento.pos):
                print("CLICK sobre boton scores")
            elif menu_principal.rectangulo_nombre.collidepoint(evento.pos):
                print("CLICK sobre boton nombre")
        
        if not menu_principal.visible:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    menu_pausa.visible = not menu_pausa.visible
                    menu_pausa.juego_pausado = not menu_pausa.juego_pausado
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if menu_pausa.rectangulo_abandonar.collidepoint(evento.pos):
                    menu_principal.visible = True
                    menu_pausa.juego_pausado = True
                    reiniciar_juego = True
                    print("CLICK sobre boton abandonar")

            if not menu_pausa.juego_pausado:
                if evento.type == pygame.USEREVENT:
                    #Evento del tiempo
                    if evento.type == timer_segundos:
                        camino_1.mover(-600)
                        camino_2.mover(-600)
                        camino_3.mover(-600)

                        bosque_izq_1.mover(-500)
                        bosque_izq_2.mover(-500)
                        bosque_izq_3.mover(-500)

                        bosque_der_1.mover(-530)
                        bosque_der_2.mover(-530)
                        bosque_der_3.mover(-530)
                        
                        moto_enemiga_1.mover()
                        moto_enemiga_2.mover()

                        mancha_aceite.mover()
            
            if auto_principal.vidas == 0:
                """Mostrar pantalla de perdida"""
                menu_perdida.visible = True
                menu_pausa.juego_pausado = True
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if menu_perdida.rectangulo_abandonar.collidepoint(evento.pos):
                        menu_perdida.visible = False
                        menu_principal.visible = True
                        reiniciar_juego = True
                        print("CLICK sobre boton abandonar")

                    elif menu_perdida.rectangulo_reintentar.collidepoint(evento.pos):
                        menu_principal.visible = False
                        menu_pausa.juego_pausado = False
                        menu_perdida.visible = False
                        reiniciar_juego = True
                        print("CLICK sobre boton reintentar")

        #Aca podes ir poniendo otras condiciones con otros eventos.

    #movemos el auto principal si el juego no esta en pausa y si no esta en el menu principal
    if not menu_pausa.juego_pausado and not menu_principal.visible:
        auto_principal.mover()

    #eliminamos corazones si colisiona con alguna de las dos motos
    if puede_colisionar:
        eliminar_corazon(auto_principal.rectangulo, moto_enemiga_1.rectangulo, auto_principal, corazon_1, corazon_2, corazon_3)
        eliminar_corazon(auto_principal.rectangulo, moto_enemiga_2.rectangulo, auto_principal, corazon_1, corazon_2, corazon_3)

    
    if reiniciar_juego:
        # aparitr de aca reinicio todos los objetos o variables a estado inicial
        camino_1 = Fondo(posicion_carretera_1)
        camino_2 = Fondo(posicion_carretera_2)
        camino_3 = Fondo(posicion_carretera_3)
        bosque_izq_1 = Fondo(posicion_bosque_izq_1)
        bosque_izq_2 = Fondo(posicion_bosque_izq_2)
        bosque_izq_3 = Fondo(posicion_bosque_izq_3)
        bosque_der_1 = Fondo(posicion_bosque_der_1)
        bosque_der_2 = Fondo(posicion_bosque_der_2)
        bosque_der_3 = Fondo(posicion_bosque_der_3)
        moto_enemiga_1 = MotoRival(posicion_moto_1, foto_moto_1)
        moto_enemiga_2 = MotoRival(posicion_moto_2, foto_moto_2)
        mancha_aceite = Aceite()
        corazon_1 = Corazon(posicion_corazon)
        corazon_2 = Corazon(posicion_corazon_2)
        corazon_3 = Corazon(posicion_corazon_3)
        menu_pausa.reiniciar()
        juego_pausado = True
        reiniciar_juego = False 
        # reinicio posición del auto principal
        auto_principal.reiniciar()
        # reinicio posición de las motos rivales
        moto_enemiga_1.reiniciar(-120)
        moto_enemiga_2.reiniciar(-820)
        # reinicio posicion de mancha de aceite
        mancha_aceite.reiniciar()

    #color del fondo
    pantalla.fill(color_verde)

    #cargamos fotos
    camino_1.dibujar(pantalla, foto_carretera)
    camino_2.dibujar(pantalla, foto_carretera)
    camino_3.dibujar(pantalla, foto_carretera)

    bosque_izq_1.dibujar(pantalla, foto_bosque_izq)
    bosque_izq_2.dibujar(pantalla, foto_bosque_izq)
    bosque_izq_3.dibujar(pantalla, foto_bosque_izq)

    bosque_der_1.dibujar(pantalla, foto_bosque_der)
    bosque_der_2.dibujar(pantalla, foto_bosque_der)
    bosque_der_3.dibujar(pantalla, foto_bosque_der)

    moto_enemiga_1.dibujar(pantalla)
    moto_enemiga_2.dibujar(pantalla)

    mancha_aceite.dibujar(pantalla)

    auto_principal.dibujar(pantalla)

    corazon_1.dibujar(pantalla)
    corazon_2.dibujar(pantalla)
    corazon_3.dibujar(pantalla)

    menu_principal.dibujar(pantalla)

    menu_pausa.dibujar(pantalla)

    menu_perdida.dibujar(pantalla)

    #modificamos los cambios
    pygame.display.flip()

pygame.quit()