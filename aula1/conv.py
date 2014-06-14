# coding: utf-8

"""
Função genérica para converter valores de uma faixa de entrada para
uma faixa de saída.

Exemplos de uso
---------------

Conversão de temperatura agradável de Celsius para Fahrenheit:

    >>> conv(22, 0, 100, 32, 212)
    71.6

Conversão de temperatura desagradável de Fahrenheit para Celsius:

    >>> conv(0, 32, 212, 0, 100)  # doctest: +ELLIPSIS
    -17.77777...

Usando apenas os argumentos default para produzir uma porcentagem:

    >>> a = 3
    >>> b = 12
    >>> conv(float(a)/b)  # em Python 3 é desnecessário este `float()`
    25.0

Limitando apenas o valor máximo da entrada:

    >>> a = 3
    >>> conv(a, entrada_max=12)
    25.0

    >>> a = 3
    >>> conv(a, entrada_max=9)  # doctest: +ELLIPSIS
    33.333333...

Inversão da saída:

    >>> conv(3, 0, 10, 10, 0)
    7.0
    >>> conv(3, 0, 10, 100, 0)
    70.0
    >>> conv(3, 1, 10, 10, 1)
    8.0

Implementação
-------------

A função ``conv`` é análoga à função ``map`` da biblioteca padrão do
Arduino. A diferença mais importante é que ``conv`` faz toda a sua
aritmética em ``float``, e devolve sempre um ``float`` como resultado,
enquanto ``map`` trabalha com o tipo ``long`` do C++, semelhante ao
``int`` de Python.

Esta é a implementação documentada no site do Arduino
(http://arduino.cc/en/reference/map):

::

    long map(long x, long in_min, long in_max, long out_min, long out_max)
    {
      return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
    }



"""

def conv(entrada, entrada_min=0.0, entrada_max=1.0,
         saida_min=0.0, saida_max=100.0):
    fator = float(saida_max - saida_min) / (entrada_max - entrada_min)
    return (entrada - entrada_min) * fator + saida_min
