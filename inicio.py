"""
1) Este archivo tiene el fondo y el auto en movimiento.

2) El auto ya tiene configurado las teclas para moverse turbo o volver a normal y tambien tiene los topes
   para que no se salga del camino.

3) clase creada para el auto principal.

4) Las motos rivales tienen su propia clase.
    Motos rivales funcionan perfecto y aparecen de forma random

5) Ordene el codigo, meti todo en el archivo nuevo de clases.

6) Colisiones con motos y aceite configuradas
    Pasado todo a archivo constantes
    Foto aceite

7) Elimine la tercera moto
    Arrelgue funcion de colisiones y actualizar posicion rects

8) Funciona perfecto el menu de pausa.

Cosas por hacer:
colisiones con autos rivales.
sonidos de colisiones y turbo.
seleccionar el auto para jugar

quizas una clase para el fondo?

programar menu: en este se tiene que seleccionar jugar o ver record historico.

configurar pausa dentro de la partida

poner temporizador y quizas vidas dsp de las colisiones.
"""
import pygame
import time
from constantes import *
from clases.Auto import Auto
from clases.Fondo import Fondo
from clases.MotoRival import MotoRival
from clases.Aceite import Aceite
from clases.Corazon import Corazon
from clases.Pausa import Pausa
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

#JUEGO PAUSADO
juego_pausado = False

#MENU INICIAL


flag_correr = True
while flag_correr:
    #que traiga todos los eventos y los guarde en una lista.
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        #detectamos la salida.
        if evento.type == pygame.QUIT:
            flag_correr = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                menu_pausa.visible = not menu_pausa.visible
                juego_pausado = not juego_pausado

        if not juego_pausado:
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
        #Aca podes ir poniendo otras condiciones con otros eventos.

    #movemos el auto principal si el juego no esta en pausa
    if not juego_pausado:
        auto_principal.mover()

    #eliminamos corazones si colisiona con alguna de las dos motos
    eliminar_corazon(auto_principal.rectangulo, moto_enemiga_1.rectangulo, auto_principal, corazon_1, corazon_2, corazon_3)
    eliminar_corazon(auto_principal.rectangulo, moto_enemiga_2.rectangulo, auto_principal, corazon_1, corazon_2, corazon_3)

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

    auto_principal.dibujar(pantalla)

    moto_enemiga_1.dibujar(pantalla)
    moto_enemiga_2.dibujar(pantalla)

    mancha_aceite.dibujar(pantalla)

    corazon_1.dibujar(pantalla)
    corazon_2.dibujar(pantalla)
    corazon_3.dibujar(pantalla)

    menu_pausa.dibujar(pantalla)

    #modificamos los cambios
    pygame.display.flip()

pygame.quit()