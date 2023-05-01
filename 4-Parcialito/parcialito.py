# GUIA EJERCICIOS BASICOS CON STRINGS


# Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 

# Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".

# Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..

# Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo, por ejemplo: "H0l4, m4nd0!" -> "Hl, mnd.

# Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.

# Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".


# Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"


# Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.


# Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".


# Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.

#1.Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.

def convertir_mayuscula(texto):
    texto_mayuscula = texto.upper()
    print(texto_mayuscula)



#2.Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.

def convertir_minuscula(texto):
    texto_minuscula=texto.lower()
    print(texto_minuscula)

# 3.Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.

def juntar2strings(texto1,texto2):
    texto_junto= texto1 + " " + texto2
    print(texto_junto)

# 4.Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.

def cantidad_caracteres_string(texto):
    cantidad=len(texto)
    print(cantidad)

# 5.Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.

def cantidad_de_veces_un_string(texto_repetidas, caracter):
    contador_caracter = texto_repetidas.count(caracter)
    print(contador_caracter)
#6 Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.

def lista_palabras_un_caracter(cadena, caracter):
    for valor in cadena:
        for letra in valor:
            if letra == caracter:
                print(valor)

#7 Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados

def string_espacios_eliminados(cadena):
    texto_vacio =  ""
    cadena_sin_espacios= cadena.strip().split(" ")
    for valor in cadena_sin_espacios:
        texto_vacio+=valor
    print(texto_vacio)
#8 Escribir una función que reciba dos string (nombre y apellido) y devuelva un 
# diccionario con el nombre y apellido, eliminando los espacios del comienzo y
#  el final y colocando la primer letra en mayúscula
def eliminar_espacios_principio_final_poner_mayuscula_primera_letra(texto1, texto2):
    diccionario = {}
    diccionario["nombre"] = texto1.strip().capitalize()
    diccionario["apellido"] = texto2.strip().capitalize()
    return diccionario


#9  Escribir una función que tome una lista de nombres y los una en una sola
#  cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"]
#  -> "Juan\nMaría\nPedro".
def lista_con_salto_de_linea(lista):
    cadena_con_salto= ""
    for valor in lista:
        cadena_con_salto+= "\n \n{0}".format(valor)
    print(cadena_con_salto)

# 10- Escribir una función que tome un nombre y un apellido y devuelva un
# email en formato "inicial_nombre.apellido@utn-fra.com.ar".

def nombre_apellido_con_formato(nombre, apellido):
    print("{0}_{1}.{2}@utn-fra.com.ar".format(nombre[:1],nombre,apellido))

#11 Escribir una función que tome una lista de palabras y devuelva un string
#  que contenga todas las palabras concatenadas con comas y "y" antes de la
#  última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"]
# , el string resultante debería ser "manzanas, naranjas y bananas"..
def concatenar_palabras(lista_palabras):
    separador = ", "
    if len(lista_palabras) == 0:
        return ""
    elif len(lista_palabras) == 1:
        return lista_palabras[0]
    else:
        palabras_menos_ultima = separador.join(lista_palabras[:-1])   # Une todas las palabras menos la última con comas y un espacio como separadores
        ultima_palabra = lista_palabras[-1]   # Obtiene la última palabra de la lista
        return "{0} y {1}".format(palabras_menos_ultima,ultima_palabra)  # Retorna todas las palabras concatenadas con comas y "y" antes de la última palabra



#1
texto1 = "hola"
convertir_mayuscula(texto1)
#2
texto2 = "HOLA"
convertir_minuscula(texto2)
#3
juntar2strings(texto1,texto2)
#4
cantidad_caracteres_string(texto1)
#5
texto_repetidas= "tarta"
cantidad_de_veces_un_string(texto_repetidas, caracter="a")
#6
cadena= "Ese queso es un buen queso"
cadena_cortada= cadena.split(" ")
lista_palabras_un_caracter(cadena_cortada, caracter= "u")
#7

cadena_con_espacios= "   Hola sin espacios de lados    "
string_espacios_eliminados(cadena_con_espacios)

#8
nombre = "    matías   "
apellido= "  velazco  "
nombre_apellido_recortado= eliminar_espacios_principio_final_poner_mayuscula_primera_letra(nombre,apellido)
print(nombre_apellido_recortado)

#9 
lista_de_nombres= ["Juan", "Maria", "Pedro"]
lista_con_salto_de_linea(lista_de_nombres)

#10
nombre= "martin"
apellido= "ibarra"
nombre_apellido_con_formato(nombre, apellido)

#11
lista_frutas= ["Manzanas","naranjas","bananas"]
palabras_concatenadas=concatenar_palabras(lista_frutas)
print(palabras_concatenadas)





