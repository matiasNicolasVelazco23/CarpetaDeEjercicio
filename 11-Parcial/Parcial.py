#  Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4] altura-fuerza-asc-desc

import re
import json
import copy
# Ejercicio tipo parcial
# Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por consola con RegEx
def leer_archivo(nombre_archivo:str):
    """_summary
    Función que lee un json, carga el archivo y lo transforma a una lista de diccionarios

    Args:
        Recibe el nombre del archivo como string

    Returns:
        Retorna la lista, que contiene una lista de diccionarios
    """
    lista= [] #declaro una lista vacía
    with open(nombre_archivo, "r") as archivo: #abrir en modo lectura -- as -- ¿qué nombre le quiero poner al archivo?
        dict = json.load(archivo)    #cargar archivo
        lista = dict["heroes"]   #tomará todas las clave:valor de dict:heroes
    return lista               #cargo todo el json como una lista, en este caso una lista de diccionarios

def normalizar_datos(lista: list) -> str:
    if len(lista) > 0:
        datos_normalizados = False
        for diccionario in lista:
            for clave, valor in diccionario.items():
                if type(valor) == str and valor.isdigit():
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
def imprimir_dato(dato):
    print(dato)


def imprimir_menu():
    """
    No recibe nada
    Y imprime el menu de opciones por pantalla de la A a la O (de los ejercicios) y Z para Salir
    Utiliza la funcion imprimir_dato    
    """
    menu = (
    "1. Listar los primeros N héroes. El valor de N será ingresado por el usuario (Validar que no supere max. de lista)\n"
    "2. Ordenar y listar héroes por altura. Preguntar al usuario si desea ordenar de manera ascendente ('asc') o "
    "descendente ('desc')\n"
    "3. Ordenar y listar héroes por fuerza. Preguntar al usuario si desea ordenar de manera ascendente ('asc') o "
    "descendente ('desc')\n"
    "4. Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el "
    "promedio (preguntar al usuario la condición: 'menor' o 'mayor') y listar aquellos que cumplan con ser mayores "
    "o menores según corresponda\n"
    "5. Buscar héroes por inteligencia [good, average, high] y listar aquellos que cumplan con la búsqueda (usando RegEx)\n"
    "6. Exportar a CSV la lista de héroes ordenada según la opción elegida anteriormente [1-4]\n"
    "7. Opción 7\n")
    imprimir_dato(menu)

def opciones_menu_principal():
    """
    No recibe nada
    Se encarga de imprimir el menu de opciones y pedirle al usuario una opcion de entre todas
    validando la opcion y la retorna si da error retorna -1
    """
    imprimir_menu()
    opcion = input("Elija una opcion: ")
    if re.search("[1-7]", opcion):
        return opcion
    else:
        return -1

def listar_primeros_heroes(lista):
    """_summary_
    Devuelve una nueva lista con los primeros n elementos de la lista de héroes.

    Args:
        lista (list): Lista de héroes.

    Returns:
        list: Nueva lista que contiene los primeros n elementos de la lista de héroes.
              Si la lista original tiene menos de n elementos, se devuelve la lista completa.
    """
    n = int(input("Ingrese el número de héroes a listar: "))
    if n > len(lista):
        print("El valor ingresado supera el máximo de la lista.")
    else:
        print("Primeros {0} héroes:".format(n))
        for i in range(n):
            print(lista[i]["nombre"])

def ordenar_y_listar_por_dato(lista, clave):
    opcion_orden = input("Ingrese 'asc' para ordenar de manera ascendente o 'desc' para ordenar de manera descendente: ")
    if opcion_orden == "asc":
        lista_ordenada = quick_sort(lista, clave, True)
    elif opcion_orden == "desc":
        lista_ordenada = quick_sort(lista, clave, False)
    else:
        print("Opción inválida")
        return

    print(f"Héroes ordenados por {clave}:")
    for heroe in lista_ordenada:
        valor = heroe[clave]
        print(f"Nombre: {heroe['nombre']}, {clave.capitalize()}: {valor}")
    
    if opcion_orden == "asc":
        tipo_orden= "asc"
    else:
        tipo_orden= "desc"
    nombre_archivo = f"heroes_{clave}_{tipo_orden}.csv"

    exportar_a_csv(lista_ordenada, nombre_archivo)

def exportar_a_csv(lista, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        archivo.write("clave,nombre\n")

        for heroe in lista:
            clave = "nombre"
            nombre = heroe["nombre"]

            linea = f"{clave},{nombre}\n"
            archivo.write(linea)


def quick_sort(lista_original, clave, flag_orden):
    lista_de = []
    lista_iz = []

    if len(lista_original) <= 1:
        return lista_original
    else:
        pivot = lista_original[0]

        for elemento in lista_original[1:]:
            if elemento[clave] > pivot[clave]:
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)

    if flag_orden:
        lista_iz = quick_sort(lista_iz, clave, True)
        lista_iz.append(pivot)
        lista_de = quick_sort(lista_de, clave, True)
        lista_iz.extend(lista_de)
        return lista_iz
    else:
        lista_iz = quick_sort(lista_iz, clave, False)
        lista_de.append(pivot)
        lista_de = quick_sort(lista_de, clave, False)
        lista_de.extend(lista_iz)
        return lista_de

def calcular_promedio(lista):
    # Pregunta al usuario la clave y la condición
    clave = input("Ingrese la clave numérica a promediar: ")
    condicion = input("Ingrese la condición ('menor' o 'mayor'): ")

    # Calcula el promedio
    suma_valores = 0
    contador_valores = 0
    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float:
            suma_valores += heroe[clave]
            contador_valores += 1

    promedio = suma_valores / contador_valores

    # Filtra los héroes según la condición
    heroes_filtrados = []
    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float:
            if (condicion == "menor" and heroe[clave] < promedio) or (condicion == "mayor" and heroe[clave] > promedio):
                heroes_filtrados.append(heroe)

    # Imprime los héroes filtrados
    print(f"Héroes con {clave} {condicion} al promedio:")
    for heroe in heroes_filtrados:
        print(f"Nombre: {heroe['nombre']}, {clave.capitalize()}: {heroe[clave]}")

def buscar_heroes_por_inteligencia(lista):
    patron = input("Ingrese el nivel de inteligencia (good, average, high): ")

    heroes_encontrados = []
    for heroe in lista:
        if re.search(r"\b{}\b".format(patron), heroe["inteligencia"]):
            heroes_encontrados.append(heroe)

    print(f"Héroes con inteligencia {patron}:")
    for heroe in heroes_encontrados:
        print(f"Nombre: {heroe['nombre']}, Inteligencia: {heroe['inteligencia']}")

def menu_de_opciones(lista:list):
    ordenamiento_realizado = False
    orden_actual = ""

    normalizar_datos(lista)
    while True:
            opcion = opciones_menu_principal()
            if opcion == "1":
                copia_lista = copy.deepcopy(lista)
                listar_primeros_heroes(copia_lista)
            elif opcion == "2":
                copia_lista_ej2 = copy.deepcopy(lista)
                orden2=ordenar_y_listar_por_dato(copia_lista_ej2, "altura")
                ordenamiento_realizado = True
                orden_actual = "altura"
            elif opcion == "3":
                orden3=copia_lista_ej3 = copy.deepcopy(lista)
                ordenar_y_listar_por_dato(copia_lista_ej3, "fuerza")
                ordenamiento_realizado = True
                orden_actual = "altura"
            elif opcion == "4":
                copia_lista_ej4 = copy.deepcopy(lista)
                calcular_promedio(copia_lista_ej4)
            elif opcion == "5":
                copia_lista_ej5 = copy.deepcopy(lista)
                buscar_heroes_por_inteligencia(copia_lista_ej5)
            elif opcion == "6":
                if ordenamiento_realizado:
                    nombre_archivo = f"heroes_{orden_actual}.csv"
                    exportar_csv_existente(nombre_archivo)
                else:
                    print("No se ha realizado ningún ordenamiento previo")    
                
            elif opcion == "7":
                break
            else:
                print("Opcion inválida")

def exportar_csv_existente(nombre_archivo):
    exportar_a_csv([], nombre_archivo)  # Aquí pasas una lista vacía, ya que solo quieres mostrar el archivo existente
    print(f"El archivo CSV {nombre_archivo} ha sido exportado nuevamente")

lista_heroes = leer_archivo(r"C:\Users\velaz\Desktop\M\PythonEjercicios\11-Parcial\data_stark.json")
copia_lista_heroes = copy.deepcopy(lista_heroes)
menu_de_opciones(lista_heroes)

