import re
import json
from stark_biblioteca02 import imprimir_dato
from stark_biblioteca02 import stark_normalizar_datos


# Crear la función "imprimir_menu_desafio_5" que imprima el menú de opciones por 
# pantalla (las opciones son las que se van a utilizar para acceder a la funcionalidad
#            de los puntos A hasta el O y Z para salir).  
# Reutilizar la función 'imprimir_dato' realizada en una práctica anterior.

def imprimir_menu_desafio():
    """
    No recibe nada
    Y imprime el menu de opciones por pantalla de la A a la O (de los ejercicios) y Z para Salir
    Utiliza la funcion imprimir_dato    
    """
    menu = "A.\nB.\nC.\nD.\nE.\nF.\nG.\nH.\nI.\nJ.\nK.\nL.\nM.\nN.\nO.\nZ."
    imprimir_dato(menu)

#1.2
def imprimir_menu_desafio_5():
    """
    No recibe nada
    Y imprime el menu de opciones por pantalla de la A a la O (de los ejercicios) y Z para Salir
    Utiliza la funcion imprimir_dato    
    """
    menu = "A.\nB.\nC.\nD.\nE.\nF.\nG.\nH.\nI.\nJ.\nK.\nL.\nM.\nN.\nO.\nZ."
    imprimir_dato(menu)

#1.2
def stark_menu_principal_desafio_5():
    """
    No recibe nada
    Se encarga de imprimir el menu de opciones y pedirle al usuario una opcion de entre todas
    validando la opcion y la retorna si da error retorna -1
    """
    imprimir_menu_desafio_5()
    opcion = input("Elija una opcion: ").upper()
    if re.search("[A-Z]", opcion):
        return opcion
    else:
        return -1


#1.3
def stark_marvel_app_5(lista:list):
    """
    Recibe una lista
    Y se encarga de la ejecucion principal del programa
    """
    stark_normalizar_datos(lista)
    while True:
        opcion = stark_menu_principal_desafio_5()
        if opcion == "A":
            stark_guardar_heroe_genero(lista, "M")
        elif opcion == "B":
            stark_guardar_heroe_genero(lista, "F")
        elif opcion == "C":
            stark_calcular_imprimir_guardar_heroe_genero(lista, "altura", "maximo", "M")
        elif opcion == "D":
            stark_calcular_imprimir_guardar_heroe_genero(lista, "altura", "maximo", "F")
        elif opcion == "E":
            stark_calcular_imprimir_guardar_heroe_genero(lista, "altura", "minimo", "M")
        elif opcion == "F":
            stark_calcular_imprimir_guardar_heroe_genero(lista, "altura", "minimo", "F")
        elif opcion == "G":
            stark_calcula_imprimir_guardar_promedio_altura_genero(lista, "altura", "M")
        elif opcion == "H":
            stark_calcula_imprimir_guardar_promedio_altura_genero(lista, "altura", "F")
        elif opcion == "I":
            stark_calcular_imprimir_guardar_heroe_genero(lista, "altura", "maximo", "M")
            stark_calcular_imprimir_guardar_heroe_genero(lista, "altura", "maximo", "F")
            stark_calcular_imprimir_guardar_heroe_genero(lista, "altura", "minimo", "M")
            stark_calcular_imprimir_guardar_heroe_genero(lista, "altura", "minimo", "F")
        elif opcion == "J":
            stark_calcular_cantidad_por_tipo(lista, "color_ojos")
        elif opcion == "K":
            stark_calcular_cantidad_por_tipo(lista, "color_pelo")
        elif opcion == "L":
            stark_calcular_cantidad_por_tipo(lista, "inteligencia")
        elif opcion == "M":
            stark_listar_heroes_por_dato(lista, "color_ojos")
        elif opcion == "N":
            stark_listar_heroes_por_dato(lista, "color_pelo")
        elif opcion == "O":
            stark_listar_heroes_por_dato(lista, "inteligencia")
        elif opcion == "Z":
            break
        else:
            print("Opcion erronea")   

#1.4
# para tratar el json como una lista de diccionarios la "pasamos a stark.py", entro a dict[heroes], lo cargamos y después agarramos la lista de diccionarios
def leer_archivo(nombre_archivo:str):
    lista= [] #declaro una lista vacía
    with open(nombre_archivo, "r") as archivo: #abrir en modo lectura -- as -- ¿qué nombre le quiero poner al archivo?
        dict = json.load(archivo)    #cargar archivo
        lista = dict["heroes"]   #tomará todas las clave:valor de dict:heroes
    return lista               #cargo todo el json como una lista, en este caso una lista de diccionarios

#1.5




def guardar_archivo(archivo_extension:str, contenido:str):
    """
    Recibe un archivo extension que es un string que indica el nombre del archivo y su extension(ej: archivo.csv)
    Y tambien recibe un string que es el contenido a guardar en dicho archivo
    Se abre el archivo en modo escritura
    Retorna true si no hubo errores y en caso contrario False
    Ademas en caso de exito imprime "Se creo el archivo: nombre_archivo.csv" en caso que retorne false el mensaje dice "Error al crear el archivo: nombre_archivo"
    """
    with open(archivo_extension, "w+") as archivo:
        if archivo.write(contenido + "\n"):
            print("Se creó el archivo:", archivo_extension)
            return True
        else:
            print("Error al crear el archivo:", archivo_extension)
            return False
        

#1.6Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un string que puede contener una o muchas palabras. 
# La función deberá retornar dicho string en el cual todas y cada una de las palabras que contenga, deberán estar capitalizadas 
# (Primera letra en mayúscula).

def capitalizar_palabras (string):
    palabras = re.split(r'\s+', string)
    palabras_capitalizadas = []
    for palabra in palabras:
        palabras_capitalizadas.append(palabra.capitalize())
    resultado = ' '.join(palabras_capitalizadas)
    return resultado



#1.7 Crear la función 'obtener_nombre_capitalizado' la cual recibirá por parámetro un diccionario el cual representará a un héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera:
# Nombre: Venom
# Reutilizar 'capitalizar_palabras'

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



#--------------------------------------------------------------------------
#2.1
def es_genero(diccionario:dict, genero:str):
    """
    Recibe un diccionario que representara un heroe y un string el cual sera usado para evaluar si el heroe coincide con el genero pedido
    El genero puede ser M, F o NB
    Retorna True en caso de que cumpla False caso contrario
    """
    if genero == "M" or genero == "F" or genero == "NB":
        if diccionario["genero"] == genero:
            return True
    else:
        return False
#2.2
def stark_guardar_heroe_genero(lista:list, genero:str):
    """
    Recibe la lista de heroes y un string que representa el genero a evaluar M o F
    Y imprime solamente los heroes que coincidan con el genero
    y guarda dichos nombres en un archivo csv
    """
    heroes = []
    for heroe in lista:
        if es_genero(heroe, genero):
            heroes.append(heroe["nombre"])
            nombre_formateado = obtener_nombre_capitalizado(heroe)
            imprimir_dato(nombre_formateado)

    nombre_archivo = f"heroes_{genero}.csv"
    contenido = ",".join(heroes)
    contenido = str(contenido)
    contenido = contenido.replace(",", "\n")
    if guardar_archivo(nombre_archivo, contenido):
        return True
    else:
        return False
    






#--------------------------------------------------------------------------
#3.1
def calcular_min_genero(lista:list, key:str, genero:str):
    for heroe in lista:
        if heroe["genero"] == genero:
            min = heroe
            break
    for heroe in lista:
        if heroe["genero"] == genero:
            if heroe[key] < min[key]:
                min = heroe
    return min

def calcular_max_genero(lista:list, key:str, genero:str):
    for heroe in lista:
        if heroe["genero"] == genero:
            max = heroe
            break
    for heroe in lista:
        if heroe["genero"] == genero:
            if heroe[key] > max[key]:
                max = heroe
    return max

def calcular_max_min_dato_genero(lista:list, key:str, estado:str, genero:str):
    if estado == "maximo":
        max = calcular_max_genero(lista, key, genero)
        return max
    elif estado == "minimo":
        min = calcular_min_genero(lista, key, genero)
        return min
    
def stark_calcular_imprimir_guardar_heroe_genero(lista:list, key:str, estado:str, genero:str):
    maxmin = calcular_max_min_dato_genero(lista, key, estado, genero)
    nombre_formateado = obtener_nombre_y_dato(maxmin, key)
    string = "{0} {1}: {2}".format(estado.capitalize(), key.capitalize(), nombre_formateado)
    print(string)
    nombre_archivo = "heroes_{0}_{1}_{2}.csv".format(estado, key, genero)
    if guardar_archivo(nombre_archivo, string):
        return True
    else:
        return False

























































def sumar_dato_heroe_genero(lista:list, key:str, genero:str):
    """
    Recibe una lista tipo list, una key tipo str y un genero tipo str que puede ser M o F
    Valida que los diccionarios de la lista sean tipo dict, que no sean diccionarios vacios y que el genero del heroe sea el genero pedido
    Si cumple las condiciones realiza la suma
    Y retorna la suma del valor de la key o -1 en caso que nose cumplan las validaciones
    """
    acu_key = 0
    for e_lista in lista:
        if type(e_lista) == type(dict()) and len(e_lista) > 0:
            if e_lista["genero"] == genero:
                acu_key += e_lista[key]
        else:
            return -1
    return acu_key

def cantidad_heroes_genero(lista:list, genero:str):
    """
    Recibe la lista de heroes y un string que representa el genero
    la funcion itera y suma la cantidad de heroes que cumplan la condicion de genero pasada por parametro
    Y retorna la suma
    """
    contador_cantidad_heroes = 0
    for heroe in lista:
        if heroe["genero"] == genero:
            contador_cantidad_heroes += 1
    return contador_cantidad_heroes

def dividir(dividendo:float, divisor:float):
    resultado = dividendo / divisor
    return resultado

#4.3
def calcular_promedio_genero(lista:list, key:str, genero:str):
    """
    Recibe una lista, una key tipo str que representa la clave a sumar y un genero tipo str que puede ser M o F
    Y hace la division a partir de la funcion dividir() que recibe un dividendo y un divisor
    el dividendo se obtiene a traves de la funcion sumar_dato_heroe_genero() 
    y el divisor se obtiene a traves de la funcion cantidad_heroes_genero()
    """
    acu_key = sumar_dato_heroe_genero(lista, key, genero)
    con_key = cantidad_heroes_genero(lista, genero)
    division = dividir(acu_key, con_key)
    return division

#4.4
def stark_calcula_imprimir_guardar_promedio_altura_genero(lista:list, key:str, genero:str):
    """
    Recibe una lista de heroes, y una clave tipo str que representa el valor a sumar y un genero tipo str que puede ser M o F
    Valida que la lista no este vacia en caso de no estar vacia calcula el promedio y lo imprime formateado asi:
    Altura promedio género F: 178.45
    """
    if len(lista) > 0:
        if genero == "F" or genero == "M":
            promedio = calcular_promedio_genero(lista, key, genero)
            promedio = round(promedio, 2)
            string = "{0} promedio genero {1}: {2}".format(key.capitalize(), genero, promedio)
            imprimir_dato(string)
            nombre_archivo = "heroes_promedio_{0}_{1}.csv".format(key, genero)
            if guardar_archivo(nombre_archivo, string):
                return True
            else:
                return False
    else:
        return print("Error: Lista de heroes vacia.")



































#5.1
def calcular_cantidad_tipo(lista:list, clave:str):
    """
    Recibe una lista de heroes y una clave que representa el dato a buscar, "color_ojos", "color_pelo"
    Valida que la lista no este vacia si lo esta devuelve un diccionario asi:
    {
        "Error": “La lista se encuentra vacía”
    }
    Si no esta vacia retorna un diccionario los distintos valores del tipo de dato pasada por parametro y la cantidad de cada uno
    por ejemplo color_ojos:
    {
        "Celeste": 4,
        "Verde": 8,
        "Marron": 6
    }
    """
    if len(lista) > 0:
        diccionario_colores = {}

        for heroe in lista:
            heroe[clave] = capitalizar_palabras(heroe[clave])
            if heroe[clave] == "-":
                heroe[clave] = "No Tiene"
            if heroe[clave] not in diccionario_colores:
                diccionario_colores[heroe[clave]] = 1
            else:
                diccionario_colores[heroe[clave]] += 1
        return diccionario_colores
    else:
        diccionario_error = {}
        diccionario_error["Error"] = "La lista se encuentra vacia"
        return diccionario_error

#5.2
def guardar_cantidad_heroes_tipo(diccionario_colores:dict, dato:str):
    """
    Recibe un diccionario con todos los tipos ya sean color de pelo, de ojos y como segundo parametro el dato color_pelo, color_ojos, inteligencia
    Itera cada key del diccionario y variabiliza la key con su valor para formatearlo en un mensaje y lo guarda en un archivo
    Por ejemplo:
    "Caracteristica: color_ojos Blue - Cantidad de heroes: 9"
    """
    lista_string = []
    for color in diccionario_colores:
        string = "Caracteristica: {0}: {1} - Cantidad de heroes: {2}".format(dato, color, diccionario_colores[color])
        lista_string.append(string)

    nombre_archivo = "heroes_cantidad_{0}.csv".format(dato)

    lista_string = str(lista_string)
    lista_string = lista_string.replace("', '", "\n")
    if guardar_archivo(nombre_archivo, lista_string):
         return True
    else:
        return False

#5.3
def stark_calcular_cantidad_por_tipo(lista:list, dato:str):
    """
    Recibe una lista de heroes y un dato que sera color_ojos o color_pelo
    Usa las funciones calcular_cantidad_tipo() para saber las cantidad de cada tipo
    y guardar_cantidad_heroes_tipo() para guardar cada tipo en un archivo con un string formateado
    """
    diccionario_colores = calcular_cantidad_tipo(lista, dato)
    if(guardar_cantidad_heroes_tipo(diccionario_colores, dato)):
        return True
    else:
        return False

































#6.1
def obtener_lista_de_tipos(lista:list, dato:str):
    """
    Recibe una lista de heroes y un dato que sera color_ojos o color_pelo
    Itera la lista y guarda en una lista las variedades del tipo de dato pasado por parametro
    si encuentra un key sin valor se reemplaza por "N/A"
    Retorna la lista con todos los valores encontrados
    """
    lista_de_tipos = []
    for heroe in lista:
        heroe[dato] = capitalizar_palabras(heroe[dato])
        if heroe[dato] == "-" or heroe[dato] == "N/a":
            heroe[dato] = "N/A"
        if heroe[dato] not in lista_de_tipos:
            lista_de_tipos.append(heroe[dato])
    return lista_de_tipos

def normalizar_dato(dato:str, valor_por_defecto:str):
    """
    Recibe el valor de un dato del heroe y un str que representa el valor por defecto a colocar en caso de que el valor este vacio
    Valida que el dato no este vacio, si lo esta lo reemplaza con el valor default pasado por parametro y lo retorna
    Caso contrario lo retornara sin modificaciones
    """
    if dato == "-":
        dato = valor_por_defecto
        return dato
    else:
        return dato

def normalizar_heroe(heroe:dict, clave:str):
    """
    Recibe un diccionario que representa el heroe y la clave que debe ser normalizada
    Capitaliza las palabras que tengan dicha key como valor y si el dato esta vacia pone "N/A"
    y finalmente capitaliza todas las palabras del nombre del heroe
    """
    heroe[clave] = capitalizar_palabras(heroe[clave])
    if heroe[clave] == "-":
        normalizar_dato(heroe[clave], "N/A")
    heroe["nombre"] = capitalizar_palabras(heroe["nombre"])
    return heroe

#6.4
def obtener_heroes_por_tipo(lista:list, diccionario_tipos:dict, dato_tipo:str):
    """
    Recibe una lista y un diccionario de tipos de colores ya sea pelo o ojos y un dato a evaluar (cojor_ojos, color_pelo)
    Itera cada tipo en diccionario_tipos y si el tipo no esta en un diccionario que cree anteriormente guarda el tipo como key y una lista vacia como valor
    y itera por heroe en la lista, capitaliza los nombres y la clave pedida por parametro 
    y verifica que si la clave del heroe ya esta en diccionario_tipos_nombres que guarda el nombre del heron como valor segun el color
    """
    diccionario_tipos_nombres = {}
    for tipo in diccionario_tipos:
        if tipo not in diccionario_tipos_nombres:
            diccionario_tipos_nombres[tipo] = []
        for heroe in lista:
            heroe = normalizar_heroe(heroe, dato_tipo)
            if heroe[dato_tipo] == tipo:
                diccionario_tipos_nombres[tipo].append(heroe["nombre"])
    return diccionario_tipos_nombres

def guardar_heroes_por_tipo(diccionario_tipos:dict, tipo_dato:str):
    """
    Recibe un diccionario con los tipos o variedades de colores de ojos o pelos que contiene como key el color y como valores los nombres de los heroes con ese color
    Y un string que representa el tipo de dato ya sea color_ojos o color_pelo
    Itera cada key y cada valor y al final crea un mensaje tipo str que imprime por ej:
    "color_ojos Green: Black Widow | Hulk"
    """
    lista_mensajes_formateados = []
    for tipo in diccionario_tipos:
        string = "{0} {1}: {2}".format(tipo_dato, tipo, diccionario_tipos[tipo])
        lista_mensajes_formateados.append(string)
    nombre_archivo = f"heroes_segun_{tipo_dato}.csv"
    string_mensajes_formateados = str(lista_mensajes_formateados)
    string_mensajes_formateados = string_mensajes_formateados.replace('", ', "\n")
    if guardar_archivo(nombre_archivo, string_mensajes_formateados):
        return True
    else:
        return False

def stark_listar_heroes_por_dato(lista:list, tipo_dato:str):
    """
    Recibe una lista y un tipo de dato a evaluar por ej color_ojos, color_pelo
    y utiliza las funciones obtener_lista_de_tipos(), obtener_heroes_por_tipo(), guardar_heroes_por_tipo()
    Retorna True si se guardo el archivo
    False caso contrario
    """
    lista_de_tipos = obtener_lista_de_tipos(lista, tipo_dato)
    diccionario_tipos_nombres = obtener_heroes_por_tipo(lista, lista_de_tipos, tipo_dato)
    if guardar_heroes_por_tipo(diccionario_tipos_nombres, tipo_dato):
        return True
    else:
        return False