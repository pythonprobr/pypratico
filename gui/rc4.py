#!/usr/bin/env python3

def rc4(chave, entrada, loops=1):
    ''' Algoritmo compatível com o RC4 '''

    kbox = list(range(256)) # criar caixa para chave
    for i, car in enumerate(chave): # copiar chave e vetor
        kbox[i] = car
    j = len(chave)
    for i in range(j, 256): # repetir ate preencher
        kbox[i] = kbox[i-j]

    # [1] inicializar sbox
    sbox = list(range(256)) # criar e inicializar caixa de substituicao

    j = 0
    # repetir o embaralhamento da sbox, conforme recomendado em
    # CipherSaber-2: http://ciphersaber.gurus.com/faq.html#cs2
    for k in range(loops):
        for i in range(256):
            j = (j + sbox[i] + kbox[i] ) % 256
            sbox[i], sbox[j] = sbox[j], sbox[i]

    # LOOP PRINCIPAL
    i = 0
    j = 0
    saida = bytearray()

    for car in entrada:
        i = (i + 1) % 256
        # [2] embaralhar sbox
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        # [3] calcular t
        t = (sbox[i] + sbox[j]) % 256
        k = sbox[t]
        car = car ^ k
        saida.append(car)

    return saida

def _testes():
    from time import time
    claro = bytearray(b'1234567890' * 100000)
    t0 = time()
    cifrado = rc4(b'chave', claro)
    print("tempo acumulado: %.2f s" % (time() - t0))
    resultado = rc4(b'chave', cifrado)
    assert resultado == claro, '%r != %r' % (resultado, claro)
    print("tempo acumulado: %.2f s" % (time() - t0))
    print('OK')

if __name__=='__main__':
    _testes()

