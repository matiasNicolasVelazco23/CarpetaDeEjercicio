
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

    for heroe in lista:
        print(obtener_nombre_y_dato(heroe, 'altura'))

#--------------------------------------------------------------------
def calcular_max(lista: list, clave: str) -> dict:
    maximo_indice = 0
    for indice_actual in range(1, len(lista)):
        if lista[indice_actual][clave] > lista[maximo_indice][clave]:
            maximo_indice = indice_actual
    return lista[maximo_indice]


def calcular_min(lista: list, clave: str) -> dict:
    minimo_indice = 0
    for indice_actual in range(1, len(lista)):
        if lista[indice_actual][clave] < lista[minimo_indice][clave]:
            minimo_indice = indice_actual
    return lista[minimo_indice]

def calcular_max_min_dato(lista: list, tipo_de_dato: str, key: str):
    if tipo_de_dato == "máximo":
        return calcular_max(lista, key)
    elif tipo_de_dato == "mínimo":
        return calcular_min(lista, key)


def stark_calcular_imprimir_heroe(lista: list, tipo_de_dato: str, key: str) -> None:
    if len(lista) == 0:
        return -1
    heroe = calcular_max_min_dato(lista, tipo_de_dato, key)
    
    
    if tipo_de_dato == "máximo":
        print("Mayor {0}:  {1}".format(key,  obtener_nombre_y_dato(heroe,"altura")))
    elif tipo_de_dato == "mínimo":
        print("Menor {0}:  {1}".format(key, obtener_nombre_y_dato(heroe,"altura")))
#---------------------------------------------------------------------------


def dividir(dividendo: float, divisor: float) -> float:
    if divisor == 0:
        return 0
    else:
        return dividendo / divisor


def sumar_dato_heroe(lista_heroes: list, key: str) -> float:
    suma = 0
    for heroe in lista_heroes:
        valor = heroe[key]
        if type(valor) in (int, float):
            suma += valor
    return suma

def calcular_promedio(lista: list, dato: str) -> float:
    suma = sumar_dato_heroe(lista, dato)
    cantidad_heroes = len(lista)
    if cantidad_heroes == 0:
        return 0
    else:
        promedio = dividir(suma, cantidad_heroes)
        return promedio
    

def stark_calcular_imprimir_promedio_altura(lista_heroes: list) -> None:
    if len(lista_heroes) == 0:
        return -1

    promedio_altura = calcular_promedio(lista_heroes, 'altura')
    imprimir_dato("Altura promedio: {0}".format(promedio_altura))
#-------------------------------------------------------------------------------
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

def validar_entero(numero_str: str) -> bool:
    if type(numero_str) == str and re.match(r'^[0-9]+$', numero_str):#puedo usar tmb isdigit
        return True
    else:
        return False

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese el número de una de las opciones: ")
    if validar_entero(opcion):
        return int(opcion)
    else:
        return -1


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