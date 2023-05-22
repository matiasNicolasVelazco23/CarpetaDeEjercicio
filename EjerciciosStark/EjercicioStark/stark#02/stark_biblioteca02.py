
from data_stark import lista_personajes
import re

# Desafío #00:

# Analizar detenidamente el set de datos
# Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
# Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
# Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
# Calcular e informar cual es el superhéroe más y menos pesado.
# Ordenar el código implementando una función para cada uno de los valores informados.
# Construir un menú que permita elegir qué dato obtener

#----------------------------------------------------------------------
# Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista de héroes. La función deberá:
# Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos)
# Validar primero que el tipo de dato no sea del tipo al cual será casteado. Por ejemplo si una key debería ser entero (ejemplo edad) verificar antes que no se encuentre ya en ese tipo de dato.
# Si al menos un dato fue modificado, la función deberá imprimir como mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”

def stark_normalizar_datos(lista:list)-> str:
    if len(lista) > 0:
        datos_normalizados = False
        for diccionario in lista:
            for clave, valor in diccionario.items():
                if type(valor) == str and re.match(r'^[0-9]+$',valor):
                    valor_convertido = int(valor)
                    diccionario[clave] = valor_convertido
                    datos_normalizados = True

                elif type(valor) == str and re.match(r"(^[0-9]+)(\.|\,)([0-9]+$)", valor):#hice una función para verificar esto, puedo usarla también
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
# Nombre: Howard the Duck

def obtener_nombre(diccionario: dict)-> str: 
    return f"Nombre: {diccionario['nombre']}"


# Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y deberá imprimirlo en la consola. 
# La función no tendrá retorno.


def imprimir_dato(dato):
    print(dato)

# Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por parámetro la lista de héroes y 
# deberá imprimirla en la consola. Reutilizar las funciones hechas en los puntos 1.1 y 1.2. 
# Validar que la lista no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 1 del desafío #00
def stark_imprimir_nombre_heroes(lista: list):
    if len(lista) == 0:
        return -1
    for elemento in lista:
        nombre = obtener_nombre(elemento)
        imprimir_dato(nombre)

#--------------------------------------------------------------------
# Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener. 


# La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.


# El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)

# Nombre: Venom | fuerza: 500

def obtener_nombre_y_dato(heroe, key):
    if key in heroe:
        return f"Nombre: {heroe['nombre']} | {key}: {heroe[key]}"
    else:
        return f"No se encontró el atributo '{key}' para el héroe {heroe['nombre']}"

# Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y alturas USANDO la función creada en el punto 
# 2. Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 2 del desafío #00
def stark_imprimir_nombres_alturas(lista):
    if len(lista) == 0:
        return -1
    
    for heroe in lista:
        print(obtener_nombre_y_dato(heroe, 'altura'))

#--------------------------------------------------------------------
# Crear la función 'calcular_max' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más alto.
# Ejemplo de llamada:
# 	calcular_max(lista, 'edad')


def calcular_max(lista: list, clave: str) -> dict:
    maximo_indice = 0
    for indice_actual in range(1, len(lista)):
        if lista[indice_actual][clave] > lista[maximo_indice][clave]:
            maximo_indice = indice_actual
    return lista[maximo_indice]

# Crear la función 'calcular_min' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más bajo. 
# Ejemplo de llamada:
# 	calcular_min(lista, 'edad')
def calcular_min(lista: list, clave: str) -> dict:
    minimo_indice = 0
    for indice_actual in range(1, len(lista)):
        if lista[indice_actual][clave] < lista[minimo_indice][clave]:
            minimo_indice = indice_actual
    return lista[minimo_indice]
#----------------------------------------------------------------

# Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:


# La lista de héroes
# El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
# Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
# La función deberá retornar el héroe que cumpla con la condición pedida. Reutilizar las funciones hechas en los puntos 4.1 y 4.2
# Ejemplo de llamada:
# calcular_max_min_dato(lista, "maximo", "edad")

def calcular_max_min_dato(lista: list, tipo_de_dato: str, key: str):
    if tipo_de_dato == "máximo":
        return calcular_max(lista, key)
    elif tipo_de_dato == "mínimo":
        return calcular_min(lista, key)

# Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres parámetros: 


# La lista de héroes
# El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
# Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
# Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00
# La función deberá obtener el héroe que cumpla dichas condiciones, imprimir su nombre y el valor calculado. Reutilizar las funciones de los puntos:
# punto 1.2, punto: 2 y punto 4.3 
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Ejemplo de llamada:
#  	stark_calcular_imprimir_heroe (lista, "maximo", "edad")
#             Ejemplo de salida:
# 	Mayor altura: Nombre: Howard the Duck | altura: 79.34

def stark_calcular_imprimir_heroe(lista: list, tipo_de_dato: str, key: str) -> None:
    if len(lista) == 0:
        return -1
    heroe = calcular_max_min_dato(lista, tipo_de_dato, key)
    
    
    if tipo_de_dato == "máximo":
        print("Mayor {0}:  {1}".format(key,  obtener_nombre_y_dato(heroe,"altura")))
    elif tipo_de_dato == "mínimo":
        print("Menor {0}:  {1}".format(key, obtener_nombre_y_dato(heroe,"altura")))
#---------------------------------------------------------------------------

# Crear la función  ‘dividir’ la cual recibirá como parámetro dos números (dividendo y divisor). 
# Se debe verificar si el divisor es 0,  en caso de serlo, retornar 0, caso contrario realizar la división entre los parámetros y retornar el resultado

def dividir(dividendo: float, divisor: float) -> float:
    if divisor == 0:
        return 0
    else:
        return dividendo / divisor

# Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes y
# un string que representara el dato/key de los héroes que se requiere sumar. Validar que cada
# héroe sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. 
# La función deberá retorna la suma de todos los datos según la key pasada por parámetro

def sumar_dato_heroe(lista_heroes: list, key: str) -> float:
    suma = 0
    for heroe in lista_heroes:
        valor = heroe[key]
        if type(valor) in (int, float):
            suma += valor
    return suma

# Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes
# y un string que representa el dato del héroe que se requiere calcular el promedio. 
# La función debe retornar el promedio del dato pasado por parámetro

def calcular_promedio(lista: list, dato: str) -> float:
    suma = sumar_dato_heroe(lista, dato)
    cantidad_heroes = len(lista)
    if cantidad_heroes == 0:
        return 0
    else:
        promedio = dividir(suma, cantidad_heroes)
        return promedio
    
# Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la altura promedio. Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y 5.3
# Con este se resuelve el Ej 5 del desafío #00

def stark_calcular_imprimir_promedio_altura(lista_heroes: list) -> None:
    if len(lista_heroes) == 0:
        return -1

    promedio_altura = calcular_promedio(lista_heroes, 'altura')
    imprimir_dato("Altura promedio: {0}".format(promedio_altura))
#-------------------------------------------------------------------------------
# Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, 
# el cual permite utilizar toda la funcionalidad ya programada. 
# Se deberá reutilizar la función antes creada encargada de imprimir un string (1.2)

def imprimir_menu():
    print("Menú de opciones:\n")
    imprimir_dato("1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
    imprimir_dato("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe junto a su altura")
    imprimir_dato("3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)")
    imprimir_dato("4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)")
    imprimir_dato("5. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)")
    imprimir_dato("6. Informar el nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)")
    imprimir_dato("7. Calcular e informar cuál es el superhéroe más y menos pesado")
    imprimir_dato("8. Ordenar el código implementando una función para cada uno de los valores informados")
    imprimir_dato("0. Salir del programa\n")

# Crear la función “validar_entero” la cual recibirá por parámetro un string de 
# número el cual deberá verificar que sea sea un string conformado únicamente por dígitos. 
# Retornara True en caso de serlo, False caso contrario

def validar_entero(numero_str: str) -> bool:
    if type(numero_str) == str and re.match(r'^[0-9]+$', numero_str):#puedo usar tmb isdigit
        return True
    else:
        return False


# Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. 
# En caso de ser correcto dicho número, lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las funciones del ejercicio 6.1 y 6.2

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese el número de una de las opciones: ")
    if validar_entero(opcion):
        return int(opcion)
    else:
        return -1

# Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa. 

def stark_marvel_app(lista_personajes):
    stark_normalizar_datos(lista_personajes)
    while True:
        opcion = stark_menu_principal()

        if opcion == 1:
            stark_imprimir_nombre_heroes(lista_personajes)

        elif opcion == 2:
            stark_imprimir_nombres_alturas(lista_personajes)

        elif opcion == 3:
            calcular_max(lista_personajes, "altura")

        elif opcion == 4:
            calcular_min(lista_personajes, "altura")

        elif opcion == 5:
            stark_calcular_imprimir_promedio_altura(lista_personajes)

        elif opcion == 6:
            stark_calcular_imprimir_heroe(lista_personajes, "máximo", "altura")
            stark_calcular_imprimir_heroe(lista_personajes, "mínimo", "altura")

        elif opcion == 7:

            stark_calcular_imprimir_heroe(lista_personajes, "máximo", "peso")
            stark_calcular_imprimir_heroe(lista_personajes, "mínimo", "peso")

        elif opcion == 0:
            break

        else:
            print("Opción inválida. Intente de nuevo.")
            continue

        # Llamada a funciones de informar aquí

    print("Fin del programa.")