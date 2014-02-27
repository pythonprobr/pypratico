"""
Demonstração de codificação na saída padrão
"""

import unicodedata

# string to use when unicodedata.name raises ValueError
NO_SUCH_NAME = '<no such name>'
UNDEFINED = '<undefined>'
ENCODE_ERROR_MSG = 'character maps to <undefined>'

def gerar_amostra(codif, inicio=32, termino=256):
    """
    """
    amostra = []
    for i in range(inicio, termino):
        car = bytes((i,)).decode(codif)
        amostra.append(car)
    return amostra

def associar_nomes(amostra):
    nomes = [unicodedata.name(car, NO_SUCH_NAME) for car in amostra]
    return zip(amostra, nomes)

def codificar_amostra(amostra, codif, replacement=b' '):
    octetos = []
    for car in amostra:
        try:
            octetos.append(bytes(car, codif))
        except UnicodeEncodeError as exc:
            if exc.reason == ENCODE_ERROR_MSG:
                octetos.append(replacement)
            else:
                raise exc

    return octetos
