def cuenta_palabras (texto:str):
    dic_contador = {}
    lista_palabras= texto.split(" ")
    for palabra in lista_palabras:
        if palabra in dic_contador:
            dic_contador[palabra] = dic_contador[palabra] + 1
        else:
            dic_contador[palabra] = 1
    return dic_contador

texto= "hola que tal hola que         tal hola a" 
aaa= cuenta_palabras(texto)
print(aaa)