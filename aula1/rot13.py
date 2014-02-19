import sys

def rot13(texto):
    """Embaralha texto pelo método ROT13

        >>> rot13('HELLO')
        'URYYB'
        >>> rot13('hello')
        'uryyb'
        >>> rot13('Boa noite!')
        'Obn abvgr!'
        >>> rot13('Obn abvgr!')
        'Boa noite!'

    """
    saida = ''
    for letra in texto:
        if 'A' <= letra <= 'Z':
            base = ord('A')
        elif 'a' <= letra <= 'z':
            base = ord('a')
        else:
            base = None
        if base is None:
            saida += letra
        else:
            posicao = ord(letra) - base
            saida += chr((posicao+13) % 26 + base)

    return saida

def exibir(nome_arq):
    with open(nome_arq, encoding='utf-8') as arq:
        for lin in arq:
            print(rot13(lin.rstrip()))

def main(argv):
    if len(sys.argv) < 2:
        print('Modo de usar: rot13.py <nome-do-arquivo>')
        sys.exit(1)
    else:
        exibir(sys.argv[1])

if __name__=='__main__':
    main(sys.argv)
