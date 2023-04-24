# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #01 los siguientes puntos, utilizando un menú que permita acceder a cada uno de los puntos por separado.
# 1-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# 2-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# 3-Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
# 4-Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
# 5-Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
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
lista_personajes =[
  {
    "nombre": "Rocket Raccoon",
    "identidad": "Rocket Raccoon",
    "empresa": "Marvel Comics",
    "altura": "122.77",
    "peso": "25.73",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Brown",
    "fuerza": "5",
    "inteligencia": "average"
  },
  {
    "nombre": "Wolverine",
    "identidad": "Logan",
    "empresa": "Marvel Comics",
    "altura": "160.69999999999999",
    "peso": "135.21000000000001",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "Black",
    "fuerza": "35",
    "inteligencia": "good"
  },
  {
    "nombre": "Black Widow",
    "identidad": "Natasha Romanoff",
    "empresa": "Marvel Comics",
    "altura": "170.78999999999999",
    "peso": "59.340000000000003",
    "genero": "F",
    "color_ojos": "Green",
    "color_pelo": "Auburn",
    "fuerza": "15",
    "inteligencia": "good"
  },
  {
    "nombre": "Mystique",
    "identidad": "Raven Darkholme",
    "empresa": "Marvel Comics",
    "altura": "178.65000000000001",
    "peso": "54.960000000000001",
    "genero": "F",
    "color_ojos": "Yellow (without irises)",
    "color_pelo": "Red / Orange",
    "fuerza": "15",
    "inteligencia": "good"
  },
  {
    "nombre": "Spider-Man",
    "identidad": "Peter Parker",
    "empresa": "Marvel Comics",
    "altura": "178.28",
    "peso": "74.25",
    "genero": "M",
    "color_ojos": "Hazel",
    "color_pelo": "Brown",
    "fuerza": "55",
    "inteligencia": "high"
  }
]

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


while True:
    respuesta_str = input("\n 1 \n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9 \n 10 \n 11 \n 12 \n 13 \n 14 \n 15\n")
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
            mas_alto_masculino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes, clave = "altura", modo= "máximo", genero = "M")
            print(mas_alto_masculino)
        case 4:
        # 4-Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
            mas_alto_femenino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes, clave = "altura", modo= "máximo", genero = "F")
            print(mas_alto_femenino)
        case 5:
        # 5-Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
            mas_bajo_masculino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes, clave = "altura", modo= "mínimo", genero = "M")
            print(mas_bajo_masculino)
        case 6:
        # 6-Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
            mas_bajo_femenino = super_heroe_mas_alto_o_bajo_masculino_o_femenino(lista_personajes, clave = "altura", modo= "mínimo", genero = "F")
            print(mas_bajo_masculino)
        case 7:
        # 7-Promedio Masculinos
            promedio_masculinos= promedio_altura_por_genero(lista_personajes,genero="M")
        case 8:
        # 8-Promedio Masculinos
            promedio_femeninos= promedio_altura_por_genero(lista_personajes,genero="F")
        case 9:
            informar_indicadores_anteriores()
        case _:
            print("Opcion no valida")
        
    input("\nPulse enter para continuar\n")