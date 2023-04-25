# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #01 los siguientes puntos, utilizando un menú que permita acceder a cada uno de los puntos por separado.
# a-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# b-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# c-Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
# d-Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
# e-Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
# 6-Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
# 7-Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
# 8-Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
# 9-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems 3 a 8)
# 10-Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# 11-Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# 12-Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
# 13-Listar todos los superhéroes agrupados por color de ojos.
# 14-Listar todos los superhéroes agrupados por color de pelo.
# 15-Listar todos los superhéroes agrupados por tipo de inteligencia
from data_stark import lista_personajes


def recorrer_lista_masculino_o_femenino(lista, genero):
    for personaje in lista: # Se itera sobre cada elemento (personaje) de la lista de personajes
        if personaje["genero"] == genero: # Se verifica si el género del personaje actual coincide con el género especificado
            print(personaje["nombre"]) # Si el género del personaje actual coincide con el género especificado, se imprime el nombre del personaje
def super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista, clave, modo, genero):
    indice_max_min = 0 # Se inicializa el índice del héroe con altura máxima o mínima en 0
    for indice_actual in range(1,len(lista)): # Se itera sobre los índices de la lista de héroes
        if lista[indice_actual]['genero'] == genero: # Se verifica si el género del héroe actual coincide con el género especificado
            if modo == "máximo": # Si se busca la altura máxima
                if(lista[indice_actual][clave] > lista[indice_max_min][clave]): # Se compara la altura del héroe actual con la altura máxima actual
                    indice_max_min = indice_actual # Si la altura del héroe actual es mayor, se actualiza el índice del héroe con altura máxima
            elif modo == "mínimo": # Si se busca la altura mínima
                if(lista[indice_actual][clave] < lista[indice_max_min][clave]): # Se compara la altura del héroe actual con la altura mínima actual
                    indice_max_min = indice_actual # Si la altura del héroe actual es menor, se ac detualiza el índice del héroe con altura mínima
    return lista[indice_max_min] # Se devuelve el héroe con altura máxima o mínima según el índice almacenado en indice_max_min
def promedio_altura_por_genero(lista, genero):
    """
    Calcula el promedio de altura de los superhéroes de un género específico en una lista dada.
    
    Args:
    lista (list): lista de diccionarios con información de los superhéroes
    genero (str): género para el cual se desea calcular el promedio de altura ("M" para masculino, "F" para femenino)
    
    Returns:
    float: promedio de altura de los superhéroes del género especificado
    """
    # Inicializar variable
    suma_alturas = 0
    
    # Recorrer la lista de personajes
    for personaje in lista:
        # Verificar si el género del personaje coincide con el género especificado
        if personaje["genero"] == genero:
            # Sumar la altura del personaje a la variable suma_alturas
            suma_alturas += float(personaje["altura"])
    
    # Calcular el promedio de altura dividiendo la suma de alturas entre la cantidad de superhéroes
    promedio = suma_alturas / len(lista)
    
    return promedio
def informar_indicadores_anteriores():
    mas_alto_masculino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes, clave="altura", modo="máximo", genero="M")
    mas_alto_femenino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes, clave="altura", modo="máximo", genero="F")
    mas_bajo_masculino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes, clave = "altura", modo= "mínimo", genero = "M")
    mas_bajo_femenino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes, clave = "altura", modo= "mínimo", genero = "F")

    print("El personaje más alto masculino es: {0}\n"
          "El personaje más alto femenino es:{1}\n"
          "El personaje más bajo masculino es:{2}\n"
          "El personaje más bajo femenino es: {3}".format(
                                                mas_alto_masculino["nombre"],
                                                mas_alto_femenino["nombre"],
                                                mas_bajo_masculino["nombre"],
                                                mas_bajo_femenino["nombre"]))

def contar_personajes_por_caracteristica(lista, clave):
    # Crear un diccionario vacío para almacenar el contador de personajes por característica
    dic_contador = {}
    # Recorrer la lista de personajes
    for personaje in lista:
        # Verificar si la clave existe en el personaje
        if clave in personaje:
            # Si la clave existe, obtener el valor de la característica
            valor_caracteristica = personaje[clave]
        else:
            # Si la clave no existe, asignar "No tiene" como valor de la característica
            valor_caracteristica = "No tiene"
        # Verificar si el valor de la característica ya existe en el diccionario contador
        if valor_caracteristica in dic_contador:
            # Si el valor de la característica ya existe en el diccionario, aumentar el contador en 1
            dic_contador[valor_caracteristica] += 1
        else:
            # Si el valor de la característica no existe en el diccionario, crear una nueva entrada con el contador en 1
            dic_contador[valor_caracteristica] = 1
    # Devolver el diccionario contador con el número de personajes por cada valor de la característica
    return dic_contador

def agrupar_personajes_por_atributo(lista_personajes, clave):
    # Crear un diccionario vacío para almacenar los personajes por el atributo dado
    personajes_por_atributo = {}

    # Recorrer la lista de personajes
    for personaje in lista_personajes:
        # Obtener el valor del atributo del personaje
        valor_atributo = personaje[clave]

        # Verificar si el valor del atributo ya está en el diccionario
        if valor_atributo in personajes_por_atributo:
            # Si el valor del atributo ya está en el diccionario, agregar el personaje a la lista correspondiente
            personajes_por_atributo[valor_atributo].append(personaje)
        else:
            # Si el valor del atributo no está en el diccionario, crear una nueva lista con el personaje y agregarla al diccionario
            personajes_por_atributo[valor_atributo] = [personaje]

    # Imprimir el diccionario
    for valor_atributo, personajes in personajes_por_atributo.items():
        print(valor_atributo + ":")
        for personaje in personajes:
            print("- " + personaje["nombre"])


while True:
    respuesta_str = input("\nA)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M"
                          "\nB)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F"
                          "\nC)Recorrer la lista y determinar cuál es el superhéroe más alto de género M"
                          "\nD)Recorrer la lista y determinar cuál es el superhéroe más alto de género F"
                          "\nE)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M"
                          "\nF)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F"
                          "\nG)Recorrer la lista y determinar la altura promedio de los  superhéroes de género M"
                          "\nH)Recorrer la lista y determinar la altura promedio de los  superhéroes de género F"
                          "\nI)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems 3 a 8)"
                          "\nJ)Determinar cuántos superhéroes tienen cada tipo de color de ojos."
                          "\nK)Determinar cuántos superhéroes tienen cada tipo de color de pelo."
                          "\nL)Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). "
                          "\nM)Listar todos los superhéroes agrupados por color de ojos."
                          "\nN)Listar todos los superhéroes agrupados por color de pelo."
                          "\nO)Listar todos los superhéroes agrupados por tipo de inteligencia")
    #FALTA VALIDAR
    respuesta_int = int(respuesta_str)
    match(respuesta_int):
        # 1-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
        case 1:
            recorrer_lista_masculino_o_femenino(lista_personajes,"M")
        case 2:
        # 2-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
            recorrer_lista_masculino_o_femenino(lista_personajes,"F")
        case 3:
        # 3-Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
            mas_alto_masculino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes, 
                                                                                  clave = "altura", modo= "máximo", genero = "M")
            print(mas_alto_masculino)
        case 4:
        # 4-Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
            mas_alto_femenino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes,
                                                                                  clave = "altura", modo= "máximo", genero = "F")
            print(mas_alto_femenino)
        case 5:
        # 5-Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
            mas_bajo_masculino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes,
                                                                                   clave = "altura", modo= "mínimo", genero = "M")
            print(mas_bajo_masculino)
        case 6:
        # 6-Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
            mas_bajo_femenino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes,
                                                                                  clave = "altura", modo= "mínimo", genero = "F")
            print(mas_bajo_masculino)
        case 7:
        # 7-Promedio Masculinos
            promedio_masculinos= promedio_altura_por_genero(lista_personajes,genero="M")
        case 8:
        # 8-Promedio Masculinos
            promedio_femeninos= promedio_altura_por_genero(lista_personajes,genero="F")
        case 9:
            informar_indicadores_anteriores()
        case 10: 
            color_de_ojos_cantidad=contar_personajes_por_caracteristica(lista_personajes,clave = "color_ojos")
            print(color_de_ojos_cantidad)
        case 11:
            color_de_pelo_cantidad=contar_personajes_por_caracteristica(lista_personajes,clave = "color_pelo")
            print(color_de_pelo_cantidad)     
        case 12:
            hereoes_inteligencia_cantidad=contar_personajes_por_caracteristica(lista_personajes,clave = "inteligencia")
            print(hereoes_inteligencia_cantidad)
        case 13:
            agrupar_personajes_por_atributo(lista_personajes, clave = "color_ojos")
        case 14:
            agrupar_personajes_por_atributo(lista_personajes, clave = "color_pelo")
        case 15:
            agrupar_personajes_por_atributo(lista_personajes, clave = "inteligencia")
        case _:
            print("Opcion no valida")
        
    input("\nPulse enter para continuar\n")

    #hacer la función más general para los puntos 10 11 12 /  13 14 15
 
    #Cambiar lo imprimido en el menú