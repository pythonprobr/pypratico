def rot13(texto):
    """Embaralha texto pelo método ROT13

        >>> rot13('HELLO')
        'URYYB'
    """
    saida = ''
    for letra in texto:
        posicao = ord(letra) - ord('A')
        saida += chr(posicao+13 % 26 + ord('A'))

    return saida

