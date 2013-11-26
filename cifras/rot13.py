"""
ROT-13: cifra para obscurecer mensagens que não
precisam ser sigilosas

Exemplo de uso da função rot13car:

    >>> rot13car('a')
    'n'
    >>> rot13car('n')
    'a'
    >>> rot13car('B')
    'O'
    >>> rot13car('O')
    'B'
    >>> rot13car('ã')
    'ã'

E agora a rot13:

    >>> rot13('Abacate')
    'Nonpngr'


"""

def rot13car(entrada):
    if ord('a') <= ord(entrada) <= ord('z'):
        base = ord('a')
    elif ord('A') <= ord(entrada) <= ord('Z'):
        base = ord('A')
    else:
        return entrada
    desloc = ord(entrada) - base
    saida = chr((desloc+13) % 26 + base)
    return saida

def rot13(entrada):
    saida = []
    for car in entrada:
        saida.append(rot13car(car))
    return ''.join(saida)

def main():
    import sys
    if len(sys.argv) == 1:
        nome_entrada = input('Nome do arquivo a obscurecer: ')
    elif len(sys.argv) == 2:
        nome_entrada = sys.argv[1]
    else:
        print('Modo de usar: rot13.py [nome_arquivo]')
        sys.exit(-1)
    print('Processando:', nome_entrada)

    arq_entrada = open(nome_entrada, 'rt')
    for linha in arq_entrada:
        linha = linha.rstrip()
        saida = rot13(linha)
        print(saida)
    arq_entrada.close()

if __name__ == '__main__':
    main()





