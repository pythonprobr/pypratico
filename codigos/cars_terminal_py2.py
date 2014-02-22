"""
Exibe os caracteres de codigo 32 a 255 suportados pelo terminal
"""

import sys

cod_saida = sys.stdout.encoding
print 'Encoding:', cod_saida

for i in range(32, 256):
    octeto = chr(i)
    car_uni = octeto.decode(cod_saida)
    print car_uni,
    if i % 32 == 31:
        print
