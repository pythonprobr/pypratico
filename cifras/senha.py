# coding: utf-8

import os
import base64


def gerar_senha(n):
    '''Gera senha de n caraceres.'''
    qt_bits = n * 6  # 64 == 2 ** 6
    qt_bytes, resto = divmod(qt_bits, 8)
    print(n, qt_bits, qt_bytes, resto)
    if resto:
        qt_bytes += 1
    octetos = os.urandom(qt_bytes)
    return base64.b64encode(octetos)[:n]

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        num_cars = int(sys.argv[1])
    else:
        num_cars = 12
    print(gerar_senha(num_cars))
