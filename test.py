# Crear la función es_fecha que reciba dos string, el primero representa la expresión a evaluar y el segundo el separador de la fecha (puede ser la barra / o el guión -) y que devuelva True en caso de tratarse de una fecha válida y False en el caso contrario. Los formatos admitidos son: ‘dd/mm/aaaa’ o ‘dd-mm-a
import re

def capitalizar_palabras (string):
    palabras = re.split(r'\s+', string)
    palabras_capitalizadas = []
    for palabra in palabras:
        palabras_capitalizadas.append(palabra.capitalize())
    resultado = ' '.join(palabras_capitalizadas)
    return resultado

def obtener_nombre_capitalizado(diccionario:dict) -> str:
    """
    Recibe un diccionario el cual representara a un heroe
    Y devolvera un string el cual contenga el nombre formateado de la siguiente manera:
    Nombre: Venom
    """
    nombre_capitalizado = capitalizar_palabras(diccionario["nombre"])
    string = "Nombre: {0}".format(nombre_capitalizado)
    return string

def obtener_nombre_y_dato(diccionario:dict, clave:str):
    """
    Recibe un diccionario el cual representara un heroe y una clave de tipo str la cual representa la clave a imprimir del heroe
    La funcion devolvera un string el cual contenga el nombre y dato (clave) del heroe a imprimir
    El dato puede ser "altura", "fuerza", "peso"
    Ejemplo: Nombre: Venom | Fuerza: 500
    """
    heroe_nombre = obtener_nombre_capitalizado(diccionario)
    string = "{0} | {1}: {2}".format(heroe_nombre, clave.capitalize(), diccionario[clave])
    return string

obtener_nombre_capitalizado()