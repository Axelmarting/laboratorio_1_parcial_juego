"""
Errores:
Funciona perfecto.

Cosas por hacer de consigna:
Terminado.

Cosas no tan importantes:
seleccionar el auto para jugar
carril de reincorporacion.
tiempo para estar en el carril de reincorporacion
restar tiempo(puntaje) si pisas un pozo o otra cosa
musica de menu principal
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
from clases.Nombre import Nombre
from clases.scores import Scores
from funciones import eliminar_corazon,cargar_scores,scores_exportar_json,ordenar_scores,colision_con_aceite,reproducir_musica

pygame.init()

#TIMER
timer_segundos = pygame.USEREVENT 
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

#CREACION MENU NOMBRE
menu_nombre = Nombre()

#CREACION MENU SCORES
menu_score = Scores()

#Puede colisionar
"""
Creo esta variable ya que cuando toco jugar automaticamente me borra un corazon, con esto se soluciona
"""
puede_colisionar = False

#reinicio de juego para cuando toque abandonar
reiniciar_juego = False

# #INGRESO DE TEXTO DEL USUARIO
font_input = pygame.font.SysFont("Arial",60)
ingreso = ''
rectangulo_ingreso = pygame.Rect(350,400,270,100)

#tiempo para score
reloj = pygame.time.Clock()

#CARGO LISTA SCORES
lista_scores = cargar_scores(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\ordenado\scores.json")
lista_ordenada = ordenar_scores(lista_scores)
print(lista_ordenada)

#CARGO SONIDO
sonido_game_over = reproducir_musica()


flag_correr = True
while flag_correr:
    #que traiga todos los eventos y los guarde en una lista.
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        #detectamos la salida.
        if evento.type == pygame.QUIT:
            flag_correr = False
        
        #ACA PONGO TODO LO QUE NO ES RELACIONADO AL JUEGO

        if evento.type == pygame.MOUSEBUTTONDOWN and menu_principal.visible:
            if menu_principal.rectangulo_jugar.collidepoint(evento.pos): #boton jugar del menu principal
                print("CLICK sobre boton jugar")
                menu_principal.visible = False
                menu_pausa.juego_pausado = False
                puede_colisionar = True   
                contar_tiempo = True
            elif menu_principal.rectangulo_scores.collidepoint(evento.pos): #boton scores del menu principal
                print("CLICK sobre boton scores")
                menu_principal.visible = False
                menu_pausa.juego_pausado = True
                lista_ordenada = ordenar_scores(lista_scores)
                menu_score.visible = True
            elif menu_principal.rectangulo_nombre.collidepoint(evento.pos): #boton nombre del menu principal
                print("CLICK sobre boton nombre")
                menu_principal.visible = False
                menu_pausa.juego_pausado = True
                menu_nombre.visible = True
    
        if menu_score.visible:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if menu_score.rectangulo_finalizar.collidepoint(evento.pos): #boton finalizar del menu nombre
                    menu_principal.visible = True
                    menu_pausa.juego_pausado = True
                    menu_score.visible = False
                    print("CLICK sobre boton finalizar")

        if menu_nombre.visible:            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1] #borrar nombre del menu nombre
                else:
                    ingreso += evento.unicode #escrbir nombre del menu nombre
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if menu_nombre.rectangulo_finalizar.collidepoint(evento.pos): #boton finalizar del menu nombre
                    menu_principal.visible = True
                    menu_pausa.juego_pausado = True
                    menu_nombre.visible = False
                    print("CLICK sobre boton finalizar")

        #ACA PONGO TODO LO RELACIONADO AL JUEGO

        if not menu_principal.visible and not menu_nombre.visible:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    menu_pausa.visible = not menu_pausa.visible
                    menu_pausa.juego_pausado = not menu_pausa.juego_pausado     
            if evento.type == pygame.MOUSEBUTTONDOWN and menu_pausa.visible:
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
                contar_tiempo = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if menu_perdida.rectangulo_abandonar.collidepoint(evento.pos):
                        menu_perdida.visible = False
                        menu_principal.visible = True
                        menu_pausa.juego_pausado = True
                        nombre_jugador = ingreso
                        score = {"nombre": nombre_jugador, "tiempo": segundos}
                        lista_scores.append(score)
                        scores_exportar_json(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\ordenado\scores.json",lista_scores)
                        sonido_game_over.play()
                        reiniciar_juego = True
                        print("CLICK sobre boton abandonar")
                    elif menu_perdida.rectangulo_reintentar.collidepoint(evento.pos):
                        menu_principal.visible = False
                        menu_pausa.juego_pausado = False
                        menu_perdida.visible = False
                        reiniciar_juego = True
                        contar_tiempo = True
                        print("CLICK sobre boton reintentar")

        #Aca podes ir poniendo otras condiciones con otros eventos.

    #movemos el auto principal si el juego no esta en pausa y si no esta en el menu principal
    if not menu_pausa.juego_pausado and not menu_principal.visible:
        auto_principal.mover()

    #eliminamos corazones si colisiona con alguna de las dos motos
    if puede_colisionar:
        colision_con_aceite(auto_principal,auto_principal.rectangulo,mancha_aceite.rectangulo)
        eliminar_corazon(auto_principal.rectangulo, moto_enemiga_1.rectangulo, auto_principal, corazon_1, corazon_2, corazon_3)
        eliminar_corazon(auto_principal.rectangulo, moto_enemiga_2.rectangulo, auto_principal, corazon_1, corazon_2, corazon_3)

    if not menu_pausa.juego_pausado and contar_tiempo:
        tiempo = font_input.render("TIEMPO: {0}".format(segundos),True,color_rojo)
        tiempo_calculo_seg += 1

        if tiempo_calculo_seg == 58:
            tiempo_calculo_seg = 0
            segundos += 1


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
        # menu_pausa.juego_pausado = True
        reiniciar_juego = False 
        # reiniciio posición del auto principal
        auto_principal.reiniciar()
        # reinicio posición de las motos rivales
        moto_enemiga_1.reiniciar(-120)
        moto_enemiga_2.reiniciar(-820)
        # reinicio posicion de mancha de aceite
        mancha_aceite.reiniciar()
        segundos = 0

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

    menu_nombre.dibujar(pantalla,font_input,ingreso,rectangulo_ingreso)

    if not menu_pausa.juego_pausado and not menu_principal.visible and not menu_perdida.visible:
        pantalla.blit(tiempo,(700,10))

    menu_score.dibujar(pantalla,lista_ordenada,font_input)

    #modificamos los cambios
    pygame.display.flip()

pygame.quit()