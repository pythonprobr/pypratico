"""
Cifra XOR

Aplica ciclicamente um XOR combinando os bytes da senha com os bytes
do conteúdo.

    >>> s = 'pizza'
    >>> t = 'Garoando'
    >>> xor_decifra('pizza', xor_cifra('pizza', t))
    'Garoando'

"""

CODIF = 'utf-8'

import itertools

def xor_bytes(senha, conteudo):
    pares = zip(itertools.cycle(senha), conteudo)
    return bytes(a ^ b for a, b in pares)

def xor_cifra(senha, claro):
    saida = xor_bytes(senha.encode(CODIF), claro.encode(CODIF))
    return saida

def xor_decifra(senha, cifrado):
    saida = xor_bytes(senha.encode(CODIF), cifrado)
    return saida.decode(CODIF)





