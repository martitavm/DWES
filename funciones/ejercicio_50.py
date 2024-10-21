def redondear_puntuacion(puntuacion):
    """
    Uso una función auxiliar que redondea a dos decimales para usar map
    """
    return round(puntuacion, 2)

def calcular_medias(grupos, *args):
    """
    Calcula las medias de puntuaciones de las agrupaciones en las distintas modalidades y fases.
    Para cada agrupación, hace la media de las puntuaciones de los jurados en cada fase, y luego calcula
    la media general de todas las fases.

    Argumentos:
    grupos -- diccionario con las modalidades, agrupaciones y sus puntuaciones en las fases
    *args -- fases adicionales opcionales para agregar o modificar puntuaciones específicas

    Devuelve:
    Un diccionario con las agrupaciones y su puntuación total.
    """

    # Diccionario que almacenará las medias
    medias_agrupaciones = {}

    # Recorremos el primer diccionario (modalidades)
    for modalidad, agrupaciones in grupos.items():
        for agrupacion, fases in agrupaciones.items():
            puntuaciones_totales = []

            # Recorremos el segundo diccionario (las fases)
            for fase, puntuaciones in fases.items():
                # Redondeamos las puntuaciones a 2 decimales usando la función map
                puntuaciones_redondeadas = list(map(redondear_puntuacion, puntuaciones))

                # Calculamos la media de la fase y las guardamos en la lista puntuaciones_totales
                media_fase = sum(puntuaciones_redondeadas) / len(puntuaciones_redondeadas)
                puntuaciones_totales.append(media_fase)

            # Si hay fases adicionales en *args, las añadimos
            for fase_adicional in args:
                if fase_adicional in fases:
                    puntuaciones_adicionales = fases[fase_adicional]
                    puntuaciones_redondeadas_adicional = map(redondear_puntuacion, puntuaciones_adicionales)
                    puntuaciones_totales.append(puntuaciones_redondeadas_adicional)

            # Calculamos la media general de todas las fases de la agrupación y la almacenamos en medias_agrupaciones
            media_general = round(sum(puntuaciones_totales) / len(puntuaciones_totales), 2)
            medias_agrupaciones[agrupacion] = media_general

    return medias_agrupaciones


grupos = {
    "chirigotas": {
        "Los Yesterday": {
            "preliminares": [9.1, 9.3, 9.0, 9.2],
            "cuartos": [9.4, 9.2, 9.1, 9.3],
            "semifinal": [9.6, 9.5, 9.4, 9.5],
            "final": [9.7, 9.6, 9.8, 9.7]
        },
        "Er Chele Vara": {
            "preliminares": [8.5, 8.6, 8.7, 8.9],
            "cuartos": [8.9, 8.8, 8.6, 8.7]
        }
    },
    "comparsas": {
        "Los Ángeles Caídos": {
            "preliminares": [9.5, 9.6, 9.7, 9.8],
            "cuartos": [9.7, 9.6, 9.8, 9.9],
            "semifinal": [9.8, 9.9, 9.8, 9.9],
            "final": [9.9, 9.9, 9.8, 9.8]
        },
        "Los Millonarios": {
            "preliminares": [9.3, 9.4, 9.5, 9.6],
            "cuartos": [9.6, 9.5, 9.7, 9.8],
            "semifinal": [9.7, 9.6, 9.7, 9.8]
        }
    },
    "coros": {
        "La Trinidad": {
            "preliminares": [9.0, 9.1, 9.2, 9.3],
            "cuartos": [9.3, 9.4, 9.5, 9.6],
            "semifinal": [9.5, 9.6, 9.7, 9.8],
            "final": [9.7, 9.8, 9.9, 9.8]
        },
        "El Batallón Fletilla": {
            "preliminares": [8.8, 8.9, 9.0, 9.1],
            "cuartos": [9.0, 9.1, 9.2, 9.3],
            "semifinal": [9.2, 9.3, 9.4, 9.5]
        }
    },
    "cuartetos": {
        "Tres notas Musicales": {
            "preliminares": [9.2, 9.3, 9.1, 9.4],
            "cuartos": [9.4, 9.5, 9.3, 9.6],
            "semifinal": [9.5, 9.6, 9.7, 9.6],
            "final": [9.7, 9.8, 9.6, 9.7]
        },
        "Ser o no Ser": {
            "preliminares": [8.7, 8.8, 8.9, 8.6],
            "cuartos": [8.9, 9.0, 8.8, 8.9]
        }
    }
}

resultado = calcular_medias(grupos)
print(resultado)