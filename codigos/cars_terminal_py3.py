"""
Exibe os caracteres de codigo 32 a 255 suportados pelo terminal
"""

import sys
import codecs
import unicodedata

cod_term = sys.stdout.encoding

if len(sys.argv) == 2:
    cod_saida = sys.argv[1]
else:
    cod_saida = cod_term

info_cod_saida = codecs.lookup(cod_saida)
cod_saida = info_cod_saida.name

if cod_term.upper().startswith('UTF'):
    print('Terminal %s, exibindo caracteres Unicode: U+0020 a U+00FF' % cod_term)
    cars_uni = [chr(i) for i in range(0x20, 0x100)]
else:
    print('Terminal %s, exibindo caracteres de %s: 0x20 a 0xff' % (cod_term, cod_saida))
    cars_uni = bytes(range(0x20, 0x100)).decode(cod_saida, 'replace')

falhas = []
linha = 0x20
for i, car in enumerate(cars_uni, 0x20):
    if i % 16 == 0:
        print('%02x:' % linha, end=' ')
    try:
        print(car, end=' ')
    except UnicodeEncodeError:
        try:
            nome = unicodedata.name(car)
        except ValueError:
            print(' ', end=' ')
        else:
            if car == '\ufffd':
                # falhas.append((i, car, '<undefined>'))
                print('\x7f', end=' ')
            else:
                falhas.append((i, car, nome))
                print('*', end=' ')
    if i % 16 == 15:
        print()
        linha += 16

if falhas:
    print('* Nao exibidos (%s):' % len(falhas))
    for i, car, nome in falhas:
        print('%02x U+%04x %s' % (i, ord(car), nome))