"""
    Calcula las medias de puntuaciones de las agrupaciones en las distintas modalidades y fases.
    Para cada agrupación, hace la media de las puntuaciones de los jurados en cada fase, y luego calcula
    la media general de todas las fases.

    :param grupos: Diccionario que contiene las modalidades y agrupaciones con sus puntuaciones
    :param args: Nombre de la agrupación para la cual calcular las medias. Si no se especifica, calcula para todas
    :param fase: Fase específica para calcular media. Si no se especifica, calcula para todas las fases
    :return: Un diccionario con las agrupaciones y sus medias de puntuación total
"""
def calcular_medias(grupos, ag = None, fase = None):
   resultados = {}
   # Iteramos sobre las modalidades
   for modalidad, agrupaciones in grupos.items():
       for nombre_agrupacion, fases in agrupaciones.items():
           # Si se proporciona el argumento 'ag' y no coincide con el nombre de la agrupación, continue
           if ag and nombre_agrupacion.lower()!= ag.lower():
               continue
           medias_fases = []
           for nombre_fase, puntuaciones in fases.items():
               puntuaciones_redondeadas = list(map(lambda x: round(x,2), puntuaciones))
               media_fase = round(sum(puntuaciones_redondeadas) / len(puntuaciones_redondeadas),2)
               medias_fases.append(media_fase)

               media_total = round(sum(medias_fases) / len(medias_fases), 2)
               resultados[nombre_agrupacion] = media_total

   return resultados


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
media = calcular_medias(grupos, ag="Los Yesterday")
print(media)
