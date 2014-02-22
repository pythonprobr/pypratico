"""
Exibe os caracteres de codigo 32 a 255 suportados pelo terminal
"""

# Python >= 2.6 compatibility
from __future__ import print_function

import sys

PY2 = sys.version_info[0] == 2

def int2byte(i):
    return chr(i) if PY2 else bytes([i])

cod_saida = sys.stdout.encoding
print('Encoding:', cod_saida)

for i in range(32, 256):
    octeto = int2byte(i)
    car_uni = octeto.decode(cod_saida)
    print(car_uni, end=' ')
    if i % 32 == 31:
        print()
