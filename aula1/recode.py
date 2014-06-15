# coding: utf-8

"""
``recode`` converte bytes de uma codificação para outra.

Caso mais simples:

    >>> recode('abc', 'ASCII', 'utf-8')
    'abc'
    >>> recode('não', 'utf-8', 'iso-8859-1') == 'n\xe3o'
    True

"""

import io
import sys

def recode(bytes_ent, codif_ent, codif_sai):
    texto = bytes_ent.decode(codif_ent)
    return texto.encode(codif_sai)

def recode_arq(nome_arq, codif_ent, codif_sai):
    with io.open(nome_arq, encoding=codif_ent) as entrada:
        nome_sai = codif_sai + nome_arq
        with io.open(nome_sai, 'wt', encoding=codif_sai) as saida:
            for lin in entrada:
                saida.write(lin)
    return nome_sai

if __name__=='__main__':
    nome_arq, codif_ent, codif_sai = sys.argv[1:]
    gravado = recode_arq(nome_arq, codif_ent, codif_sai)
    print(gravado, 'gravado')

