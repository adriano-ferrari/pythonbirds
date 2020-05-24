def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('adriano')
    {'a': 2, 'd': 1, 'i': 1, 'n': 1, 'o': 1, 'r': 1}
    >>> contar_caracteres('arara')
    {'a': 3, 'r': 2}

    :param s: string a ser contada

    """

    resultado={}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado.sorted()

if __name__ == '__main__':
    print(contar_caracteres('adriano'))
    print()
    print(contar_caracteres('arara'))
