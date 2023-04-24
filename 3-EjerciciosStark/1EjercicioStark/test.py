from data_stark import lista_personajes


def encontrar_superheroe_por_genero_altx_bajx(lista, clave:str, valor:str, modo):
    superheroe_alto_o_bajo = lista[0]
    for personaje in lista:
        if personaje[clave] == valor:
            if modo == "máximo" and float(personaje["altura"]) > float(superheroe_alto_o_bajo["altura"]):
                superheroe_alto_o_bajo = personaje
            elif modo == "mínimo" and float(personaje["altura"]) < float(superheroe_alto_o_bajo["altura"]):
                superheroe_alto_o_bajo = personaje
    return superheroe_alto_o_bajo
valor_mas_bajo_m=encontrar_superheroe_por_genero_altx_bajx(lista_personajes,clave="genero", valor="M", modo= "máximo" )

valor_mas_bajo_f=encontrar_superheroe_por_genero_altx_bajx(lista_personajes,clave="genero", valor="F", modo= "mínimo" )
print(valor_mas_bajo_f)

valor_mas_bajo_Prueba=encontrar_superheroe_por_genero_altx_bajx(lista_personajes,clave="genero", valor="Prueba", modo= "mínimo" )
print(valor_mas_bajo_Prueba)