def fibonacci(n):
    print(n)
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Whiteboard Interview: ReverseCorp
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# print(lista)


def reverse(lista_numeros, contador):
    if contador >= int(len(lista_numeros) / 2):
        temp = lista_numeros[contador]
        lista_numeros[contador] = lista_numeros[-contador - 1]
        lista_numeros[-contador - 1] = temp
        contador -= 1
        reverse(lista_numeros, contador)


# reverse(lista, len(lista) - 1)
# print(lista
