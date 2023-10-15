import json


def encriptar_mensaje(mensaje: str):
    diccionario = {}

    # * Abrir diccionario.js
    with open("diccionario.json") as file:
        diccionario = dict(json.load(file))

        mensaje_encritado = ""
        diccionario = diccionario["palabras"]

        # Iterar a traves de cada letra del mensage

        for letra in mensaje:
            # Si la letra esta en el diccionario, agregar la palabra de codigo correspondiente
            if letra.upper() in diccionario:
                mensaje_encritado += diccionario[letra.upper()] + " "
            # * Si la letra no esta, agregar letra original al mensaje
            else:

                mensaje_encritado += letra
        return mensaje_encritado
