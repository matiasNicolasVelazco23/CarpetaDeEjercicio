'''
    Acción.
    Aventuras.
    Ciencia Ficción.
    Comedia.
    Documental
    Drama
    Fantasía
    Musical

[
    
    {
        'titulo': 'Volver al Futuro',
        'genero': ̈́'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'Volver al Futuro II',
        'genero': ̈́'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'Volver al Futuro III',
        'genero': ̈́'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'Volver al Futuro III',
        'genero': ̈́'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    }
]

Crear una función que recibe una lista de diccionarios con información de películas 
(título, género, director) y devuelve un diccionario con la cantidad de películas 
por género.

'''



lista_pelis = [
    {
        'titulo': 'Volver al Futuro',
        'genero': 'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'Volver al Futuro II',
        'genero': 'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'Volver al Futuro III',
        'genero': 'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'El padrino I',
        'genero': 'Drama',
        'director': 'Francis Ford Coppola'
    },
    {
        'titulo': 'El padrino II',
        'genero': 'Drama',
        'director': 'Francis Ford Coppola'
    }
]



def calcular_peliculas_por_genero2(lista_de_peliculas):

    dic_contador_generos  = {} # {'Ciencia Ficción': 3, 'Drama': 2}
    
    for pelicula in lista_de_peliculas:
        texto_genero = pelicula['genero']

        if texto_genero in dic_contador_generos:
            dic_contador_generos[texto_genero] += 1
        else:
            dic_contador_generos[texto_genero] = 1

    return dic_contador_generos


#NECESITO ENTENDER ESTO
def calcular_peliculas_por_genero(lista_de_peliculas):

    dic_contador_generos  = {} 


    
    
    for pelicula in lista_de_peliculas:
        texto_genero = pelicula['genero']
        texto_titulo = pelicula['titulo']
                
        if texto_genero in dic_contador_generos:

            dic_contador_generos[texto_genero].append(texto_titulo)
        else:
            auxiliar_lista = []
            auxiliar_lista.append(texto_titulo)
            dic_contador_generos[texto_genero] = auxiliar_lista

    return dic_contador_generos

# Por ejemplo, supongamos que tenemos la siguiente lista de películas:


# lista_pelis = [    {"titulo": "Titanic", "genero": "romance"},    {"titulo": "El Padrino", "genero": "drama"},    {"titulo": "El señor de los anillos", "genero": "fantasía"},    {"titulo": "La La Land", "genero": "romance"},    {"titulo": "Toy Story", "genero": "animación"},    {"titulo": "Forrest Gump", "genero": "drama"},    {"titulo": "Harry Potter y la piedra filosofal", "genero": "fantasía"}]
# La función calcular_peliculas_por_genero() recibe esta lista de películas como
# argumento y devuelve un diccionario que agrupa las películas por género.

# Después de procesar la primera película de la lista (Titanic), el diccionario 
# generado se verá así:

# {
#     "romance": ["Titanic"]
# }
# Para la segunda película (El Padrino), el diccionario generado se actualizará a:

# {
#     "romance": ["Titanic"],
#     "drama": ["El Padrino"]
# }
# Cuando la función procese la tercera película (El señor de los anillos), el diccionario se actualizará de nuevo a:

# {
#     "romance": ["Titanic"],
#     "drama": ["El Padrino"],
#     "fantasía": ["El señor de los anillos"]
# }
# Cuando la función procese la cuarta película (La La Land), el diccionario se actualizará así:
# {
#     "romance": ["Titanic", "La La Land"],
#     "drama": ["El Padrino"],
#     "fantasía": ["El señor de los anillos"]
# }
# Y así sucesivamente, hasta que todas las películas hayan sido procesadas y se
# haya generado el diccionario completo. En resumen, el diccionario generado agrupa 
# las películas por género, y cada valor de diccionario es una lista de títulos de películas
# correspondientes a ese género.





dic_resultado = calcular_peliculas_por_genero(lista_pelis)

for genero in dic_resultado:
    print("------------------")
    print(genero)
    print(len(dic_resultado[genero]))
    print(dic_resultado[genero])
