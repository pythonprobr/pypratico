"""
Exibe os caracteres de codigo 32 a 255 suportados pelo terminal
"""

import sys

cod_saida = sys.stdout.encoding

if cod_saida.upper().startswith('UTF'):
    print('Terminal %s, exibindo caracteres Unicode U+0020 a U+00FF' % cod_saida)
    cars_uni = [chr(i) for i in range(0x20, 0x100)]
else:
    print('Terminal %s, exibindo caracteres 0x20 a 0xff' % cod_saida)
    cars_uni = bytes(range(0x20, 0x100)).decode(cod_saida)

for i, car in enumerate(cars_uni):
    print(car, end=' ')
    if i % 32 == 31:
        print()
