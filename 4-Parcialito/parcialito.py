# GUIA EJERCICIOS BASICOS CON STRINGS
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
    # Convertimos la lista en una cadena de texto separada por comas
    cadena_texto = ",".join(cadena)
    palabras = cadena_texto.split(",")  # Separamos la cadena en una lista de palabras
    palabras_con_caracter = []
    for palabra in palabras:
        if palabra.count(caracter) > 0:  # Si la palabra tiene al menos una ocurrencia del caracter
            palabras_con_caracter.append(palabra)  # Agregamos la palabra a la lista
    return palabras_con_caracter

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

#12 
#Escribir una función que tome un número de tarjeta de crédito como input, 
# verificar que todos los caracteres sean numéricos y devolver los últimos 
# cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: 
# "**** **** **** 1234". 
def validar_tarjeta(texto):
    lista = texto.split(" ")
    flag_tarjeta_ok = True
    var_texto = "ERROR"
    for e in lista:
        if (e.isdigit() == False):
            flag_tarjeta_ok = False
            break
    if flag_tarjeta_ok and len(lista) == 4:
        var_texto = "***** {0} {1} *****". format (lista[1], lista[2])
    return var_texto

# 13. Escribir una función que tome un correo electrónico y elimine cualquier carácter d
# espués del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".
def eliminar_caracteres_despues_arroba(correo_electronico):
    correosplit = correo_electronico.split("@")
    return correosplit[0]

# 14. Escribir una función que tome una URL y devuelva solo el nombre de dominio, 
# por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
def obtener_nombre_dominio(url):
    partes_url = url.split('/')
    nombre_dominio = partes_url[2].split('.')
    return nombre_dominio[1]

# 15.Escribir una función que tome una cadena de texto y devuelva solo los caracteres 
# alfabéticos, eliminando cualquier número o símbolo, por ejemplo: "H0l4, m4nd0!" -> "Hl, mnd.
def obtener_caracteres_alfabeticos(cadena):
    caracteres_alfabeticos = ''
    for caracter in cadena:
        if caracter.isalpha():
            caracteres_alfabeticos += caracter
    return caracteres_alfabeticos
#16 Escribir una función que tome una cadena de texto y la convierta en un acrónimo, 
# tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica 
# Nacional Facultad Regional Avellaneda" -> "UTNFRA”.
def obtener_acronimo(cadena):
    acronimo = ''  # creamos una variable vacía para almacenar el acrónimo
    palabras = cadena.split()  # dividimos la cadena en palabras usando el espacio como separador y almacenamos el resultado en la variable "palabras"
    for palabra in palabras:  # iteramos sobre cada palabra en la variable "palabras"
        acronimo += palabra[0].upper()  # añadimos la primera letra de cada palabra al acrónimo, convirtiéndola a mayúscula
    return acronimo  # retornamos el acrónimo generado

#17 Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".
def convertir_a_8bits(numero_binario):
    return numero_binario.zfill(8)

#18 Escribir una función que tome una cadena de caracteres y reemplace todas 
# las letras mayúsculas por letras minúsculas y todas las letras minúsculas por 
# letras mayúsculas, por ejemplo: "HoLa" -> "hOlA
def invertir_mayusculas_minusculas(cadena):
    nueva_cadena = ""
    for caracter in cadena:
        if caracter.isupper():
            nueva_cadena += caracter.lower()
        elif caracter.islower():
            nueva_cadena += caracter.upper()
        else:
            nueva_cadena += caracter
    return nueva_cadena

#19 Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
def contar_digitos(cadena):
    contador = 0  # Inicializamos el contador de dígitos en 0
    for caracter in cadena:  # Iteramos por cada caracter de la cadena
        if caracter.isdigit():  # Si el caracter es un dígito
            contador += 1  # Aumentamos el contador en 1
    return contador  # Devolvemos el contador de dígitos encontrados


#20 Escribir una función que tome una lista de direcciones de correo electrónico y las una 
# en una sola cadena separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] 
# -> "juan@gmail.com;maria@hotmail.com".
def unir_emails(lista_emails):
    # Con el método join unimos los elementos de la lista en una cadena separada por ";"
    emails_unidos = ";".join(lista_emails)
    return emails_unidos

#21 Crear una función que reciba como parámetro un string y devuelva un diccionario
#  donde cada clave es una palabra y cada valor es un entero que indica cuántas veces
#  aparece esa palabra dentro del string.

def cuenta_palabras(texto:str): # definimos una función llamada cuenta_palabras que recibe un parámetro de tipo string llamado texto
    dic_contador = {} # creamos un diccionario vacío que se utilizará para almacenar la cantidad de veces que aparece cada palabra en el texto
    lista_palabras = texto.split(" ") # dividimos el texto en palabras separadas por espacios y las almacenamos en una lista llamada lista_palabras
    for palabra in lista_palabras: # iteramos por cada palabra de la lista_palabras
        if palabra in dic_contador: # si la palabra ya se encuentra en el diccionario
            dic_contador[palabra] = dic_contador[palabra] + 1 # aumentamos el contador de veces que aparece esa palabra en 1
        else: # si la palabra no está en el diccionario
            dic_contador[palabra] = 1 # la agregamos al diccionario con un valor de 1, indicando que apareció una vez en el texto
    return dic_contador # devolvemos el diccionario que contiene las palabras y la cantidad de veces que aparecen en el texto

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

#12
ingreso_tarjeta = input("Ingrese número de tarjeta")
validar_tarjeta(ingreso_tarjeta)
resultado_validar_tarjeta= validar_tarjeta(ingreso_tarjeta)
print(resultado_validar_tarjeta)

#13
correo_electronico = "usuario@gmail.com"
nombre_usuario = eliminar_caracteres_despues_arroba(correo_electronico)
print(nombre_usuario)  # Output: usuario

#14
url = "https://www.ejemplo.com.ar/pagina1"
nombre_dominio = obtener_nombre_dominio(url)
print(nombre_dominio)  # Output: ejemplo

#15
cadena = "H0l4, m4nd0!"
caracteres_alfabeticos = obtener_caracteres_alfabeticos(cadena)
print(caracteres_alfabeticos)  # Output: Hl mnd

#16
cadena = "Universidad Tecnológica Nacional Facultad Regional Avellaneda"
acronimo = obtener_acronimo(cadena)
print(acronimo)  # Output: UTNFRA

#17
numero_binario = "101"
numero_8bits = convertir_a_8bits(numero_binario)
print(numero_8bits)  # Output: 00000101

#18
cadena_original = "HoLa"
cadena_invertida = invertir_mayusculas_minusculas(cadena_original)
print(cadena_invertida)  # Output: "hOlA"

#19
cadena = "1234 Hola Mundo"
cantidad_digitos = contar_digitos(cadena)
print("La cantidad de dígitos en la cadena es:", cantidad_digitos)

#20
emails = ["juan@gmail.com", "maria@hotmail.com"]
resultado = unir_emails(emails)
print(resultado)
# Output: juan@gmail.com;maria@hotmail.com

#21 

texto_ejemplo = "Esta es una frase de ejemplo, y otra frase de ejemplo"
resultado = cuenta_palabras(texto_ejemplo)
print(resultado)