#!/usr/bin/env python3
# coding: utf-8

"""
qlinhas.py: identifica e converte as quebras de linha em um arquivo

Se executado com a opção -c antes do nome do arquivo, gera novo arquivo
convertendo as quebras de CR para CRLF ou vice-versa.

Funciona só em Python 3.
"""

import os
import sys

if sys.version_info.major < 3:
    print('Este programa só foi testado em Python 3')
    sys.exit(-1)

LF = '\n'
CRLF = '\r\n'

def main():
    if len(sys.argv) not in [2, 3]:
        print('Modo de usar: qlinhas.py [-c] <nome_arquivo>')
        sys.exit()
    
    nome_entrada = sys.argv[-1]
    with open(nome_entrada, 'rU') as arq_entrada:
        texto = arq_entrada.read()

    if arq_entrada.newlines is None:
        print('Nenhuma quebra de linha encontrada')
        sys.exit()  # nada a fazer

    print('Quebras de linha encontradas: %r' % arq_entrada.newlines)

    if type('arq_entrada.newlines') is tuple:
        print('Vários tipos de quebra de linha encontradas, '
              'conversão não pode ser feita')
        sys.exit(-2)

    if sys.argv[1] == '-c':
        quebra_de = arq_entrada.newlines
        if quebra_de == CRLF:
            quebra_para = LF
            tipo_saida = 'LF'
        else:
            quebra_para = CRLF
            tipo_saida = 'CRLF'
        nome, ext = os.path.splitext(nome_entrada)
        nome_saida = nome + '-' + tipo_saida + ext
        with open(nome_saida, 'wt') as arq_saida:
            saida = texto.replace(quebra_de, quebra_para)
            arq_saida.write(saida)
        print('Convertido para %r como %r' % (quebra_para, nome_saida))

if __name__=='__main__':
    main()
