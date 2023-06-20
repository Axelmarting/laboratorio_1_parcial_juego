import pygame

#LIMITE DE MOVIMIENTO
# limite_derecho = 575
# limite_izquierdo = 325
# limite_superior = 0
# limite_inferior = 550
limites_pantalla = (575, 325, 0, 550)

ancho_ventana = 1000
alto_ventana = 720
color_verde = (0, 180, 0)
color_rojo = (255, 0, 0)

velocidad_objetos = 5

#posiciones fotos
posicion_carretera_1 = [325,0]
posicion_carretera_2 = [325,520]
posicion_carretera_3 = [325,-300]

posicion_bosque_izq_1 = [-20,0]
posicion_bosque_izq_2 = [-50,400]
posicion_bosque_izq_3 = [-50,-400]

posicion_bosque_der_1 = [670,0]
posicion_bosque_der_2 = [670,400]
posicion_bosque_der_3 = [670,-400]

#Cargamos fotos y ajustamos tamanio
foto_carretera = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\ordenado\fotos\carretera.jpg")
foto_carretera = pygame.transform.scale(foto_carretera,(350,600))

foto_bosque_izq = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\ordenado\fotos\arbolesarriba-removebg-preview (1).png")
foto_bosque_izq = pygame.transform.scale(foto_bosque_izq,(350,600))

foto_bosque_der = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\ordenado\fotos\arboles_arriba_2-removebg-preview.png")
foto_bosque_der = pygame.transform.scale(foto_bosque_der,(350,600))

posicion_moto_1 = [330,-120]
posicion_moto_2 = [400,-820]

foto_moto_1 = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\ordenado\fotos\moto-removebg-preview.png")
foto_moto_1 = pygame.transform.scale(foto_moto_1,(60,100))

foto_moto_2 = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\ordenado\fotos\moto2.png")
foto_moto_2 = pygame.transform.scale(foto_moto_2,(55,95))


posicion_corazon = (10,5)
posicion_corazon_2 = (70,5)
posicion_corazon_3 = (130,5)


contar_tiempo = False
segundos = 0
tiempo_calculo_seg = 0

lista_scores = []

musica_reproduciendose = True