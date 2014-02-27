"""
Exibe os caracteres de codigo 32 a 255 da codificação ISO-8859-1 verificando
que coincidem com os codepoints 32 a 255 de Unicode
"""

import sys
import unicodedata

for i in range(32, 256):
    car = bytes((i,)).decode('ISO-8859-1')
    assert car == chr(i)
    try:
        nome = unicodedata.name(car)
    except ValueError as exc:
        nome = '<%s>' % exc
    try:
        car.encode(sys.stdout.encoding)
    except UnicodeEncodeError:
        car = ' '
        nome = '<undefined>'

    print('%3d %02x %s %s' % (i, i, car, nome))
