import random
from constantes import limites_pantalla


def generar_posicion_random()->int:
    """
    Genera un numero random el el eje x de la pantalla.
    """
    numero_random = random.randint(limites_pantalla[1], limites_pantalla[0])
    return numero_random


def actualizar_posicion_rect(clase):
    """
    Esta funcion recibe como parametro el rectangulo de la foto del auto principal y la clase del auto principal.
    Su funcion es hacer que el rectangulo de la foto se mantenga en la foto mientras esta se mueve.
    Por eso actualiza su posicion constantemente
    """
    # Actualizar la posición del rectángulo del auto principal
    clase.rectangulo.x = clase.posicion[0]
    clase.rectangulo.y = clase.posicion[1]

def pregunta_colision_vehiculo(rect_auto, rect_rival):
    """
    Recibe como parametros el rect del auto y del rival actualizados, tambien el tipo de rival con el que colisiona.
    Su funcion es preguntar si el auto colisiona con el rival y retornar True de ser asi. 
    """
    if rect_auto.colliderect(rect_rival):
        # print("colisionaste con {0}".format(tipo))
        return True
    else:
        return False


def eliminar_corazon(rect_auto, rect_rival, clase_auto: str, corazon_1, corazon_2, corazon_3):
    """
    En caso que la lista de las posiciones de los corazones no este vacia, elimina uno.
    Cuando el auto colisiona le ajusta la posicion fuera de la carretera
    Si esta vacia termina el juego.
    """

    if clase_auto.vidas > 0:
        if clase_auto.colisionando:
            return

        if pregunta_colision_vehiculo(rect_auto, rect_rival) and not clase_auto.colisionando:
            clase_auto.colisionando = True
            clase_auto.vidas -= 1
            clase_auto.posicion = [200,520]
            print("Perdiste un corazon!")
            
            if clase_auto.vidas == 2:
                corazon_3.eliminar()

            elif clase_auto.vidas == 1:
                corazon_2.eliminar()

            elif clase_auto.vidas == 0:
                corazon_1.eliminar()

            clase_auto.colisionando = False

    else:
        print("FIN DEL JUEGO")

    
    
    
