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
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('adriano'))
    print()
    print(contar_caracteres('arara'))
