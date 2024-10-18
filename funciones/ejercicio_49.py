vinos_jerez = ["Fino Sherry", "Pedro Ximénez", "Sherry Cream", "Moscatel", "Oloroso"]

def analiza_vino(*lista_vinos):
    """
        Analiza una lista de nombres de vinos y determina si contienen la palabra 'Sherry'.

        Parámetros:
        -----------
        *lista_vinos : str
            Una cantidad de nombres de vinos como argumentos.

        Devuelve:
        --------
            - d1 (dict): Un diccionario donde las claves son los nombres de los vinos y los valores
              son booleanos que indican si el vino contiene la palabra 'Sherry' (True) o no (False).
            - vinos_sherry (list): Una lista de vinos que contienen la palabra 'Sherry'.

        Ejemplo:
        --------
        >>> dic, lista_sherry = analiza_vino("Fino Sherry", "Pedro Ximénez", "Sherry Cream", "Moscatel", "Oloroso")
        >>> print(dic)
        {'Fino Sherry': True, 'Pedro Ximénez': False, 'Sherry Cream': True, 'Moscatel': False, 'Oloroso': False}
        >>> print(lista_sherry)
        ['Fino Sherry', 'Sherry Cream']
        """
    d1 = {}
    for vino in lista_vinos:
        if "Sherry" in vino:
            d1.update({vino: True})
        else:
            d1.update({vino: False})

    vinos_sherry = list(filter(lambda x: "Sherry" in x, lista_vinos))

    return d1,vinos_sherry

dic,lista_sherry = analiza_vino(*vinos_jerez)

print(dic)
print(lista_sherry)
