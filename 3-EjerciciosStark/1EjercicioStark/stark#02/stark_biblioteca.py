
from data_stark import lista_personajes
import re
#----------------------------------------------------------------------
def stark_normalizar_datos(lista:list)-> str:
    if len(lista) > 0:
        datos_normalizados = False
        for diccionario in lista:
            for clave, valor in diccionario.items():
                if type(valor) == str and re.match(r'^[0-9]+$',valor):
                    valor_convertido = int(valor)
                    diccionario[clave] = valor_convertido
                    datos_normalizados = True

                elif type(valor) == str and re.match(r"(^[0-9]+)(\.|\,)([0-9]+$)", valor):
                    valor_convertido = float(valor)
                    diccionario[clave] = valor_convertido
                    datos_normalizados = True


        if datos_normalizados:
            return "Datos normalizados"
        else:
            return "No se encontraron datos para normalizar"

    else:
        
        return "Error: Lista de héroes vacía"

#test de normalizar datos
# resultado=stark_normalizar_datos(lista_personajes)
# print(resultado)

#----------------------------------------------------------------------
# Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario 
# el cual representara a un héroe y devolverá un string el cual contenga su nombre 
# formateado de la siguiente manera: 
def obtener_nombre(diccionario: dict)-> str: 
    return f"Nombre: {diccionario['nombre']}"


def imprimir_dato(dato):
    print(dato)

def stark_imprimir_nombre_heroes(lista: list):
    if len(lista) == 0:
        return -1
    for elemento in lista:
        nombre = obtener_nombre(elemento)
        imprimir_dato(nombre)

#--------------------------------------------------------------------
def obtener_nombre_y_dato(heroe, key):
    if key in heroe:
        return f"Nombre: {heroe['nombre']} | {key}: {heroe[key]}"
    else:
        return f"No se encontró el atributo '{key}' para el héroe {heroe['nombre']}"

def stark_imprimir_nombres_alturas(lista):
    if len(lista) == 0:
        return -1
    #O   if not lista:
    #    return -1
    for heroe in lista:
        print(obtener_nombre_y_dato(heroe, 'altura'))