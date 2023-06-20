import random
import json
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
    
def colision_con_aceite(clase_auto,rect_auto, rect_aceite):
    if pregunta_colision_vehiculo(rect_auto,rect_aceite):
        posicion_random_x = random.randint(325,575)
        posicion_random_y = random.randint(0,550)
        clase_auto.posicion = [posicion_random_x,posicion_random_y]



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


def scores_exportar_json(nombre_archivo:str, lista:list):
    """
    Dos parametros: ruta de acceso y lista de datos.
    Exporta la lista de alturas casteada a str al archivo json
    """

    with open(nombre_archivo, 'w') as file:
        json.dump(lista, file, indent=4)

    print("\nLista exportada al archivo json.")

    
def obtener_tiempo(lista):
    """
    Un parametro: lista de diccionarios (lista de scores)
    Itera sobre la lista scores guardando solamente el valor de la clave tiempo en una lista de tiempos
    luego retorna la misma.
    """
    lista_tiempos = []
    for score in lista:
        tiempo = score.get('tiempo')
        lista_tiempos.append(tiempo)
    return lista_tiempos


def ordenar_scores(scores):
    """
    Recibe por parametro la lista de diccionarios con los scores
    Ordena la lista de tiempos obtenida en la funcion anterior y la ordena de manera descendente.
    Luego agrega los diccionarios ordenados a una lista que finalmente retorna.
    """
    lista_tiempos = obtener_tiempo(scores)
    lista_tiempos.sort(reverse=True) 

    lista_dicts_scores_ordenada = []
    for tiempo in lista_tiempos:
        for diccionario in scores:
            if diccionario['tiempo'] == tiempo:
                lista_dicts_scores_ordenada.append(diccionario)
                break
    return lista_dicts_scores_ordenada


    
def cargar_scores(nombre_archivo:str):
    """
    recibe un paramentro que es la ruta de acceso del archivo json donde estan los scores.
    carga la lista de scores y luego la retorna.
    (esta funcion la hice porque cuando me terminaba el juego se borraba toda la lista, no quedaba guardada.)
    """
    with open(nombre_archivo, 'r') as file:
        lista_scores = json.load(file)

    return lista_scores

