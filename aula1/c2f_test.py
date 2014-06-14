# coding: utf-8

"""
Conversão de graus Celsius para Fahrenheit e vice-versa

Este módulo foi criado para testar e demonstrar a função
genérica de conversão ``conv.conv``.
"""

from __future__ import print_function

from conv import conv

# fórmulas específicas

def c2f(c):
    return (c * 9.0 / 5) + 32

def f2c(f):
    return (f - 32) * 5.0 / 9

# testes comparando resultados da função genérica
# ``comp.comp``

TEMP_C = range(-40, 111, 10)
TEMP_F = sorted(list(range(-40, 221, 20)) + [32, 212])
EPSILON = 10e-7

def quase_igual(a, b):
    return abs(a - b) < EPSILON

def test_c2f():
    print('%7s %7s' % ('C', 'F'))
    for c in TEMP_C:
        f = c2f(c)
        print('%7.2f %7.2f' % (c, f))
        assert quase_igual(f , conv(c, 0, 100, 32, 212))

def test_f2c():
    print('%7s %7s' % ('F', 'C'))
    for f in TEMP_F:
        c = f2c(f)
        print('%7.2f %7.2f' % (f, c))
        assert quase_igual(c, conv(f, 32, 212, 0, 100))

if __name__ == '__main__':
    test_c2f()
    test_f2c()
