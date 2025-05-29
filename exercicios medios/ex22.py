# 22. Crie uma fun¸c˜ ao que recebe uma lista e retorna uma nova lista com apenas os elementos ´ unicos.

lista = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7]

def elementosunicos(lista):
    for num in lista:
        lista = set(lista)
    return lista

retorno_lista = elementosunicos(lista)
print(retorno_lista)
