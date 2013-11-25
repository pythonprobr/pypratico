# coding: utf-8

"""Cifra XOR

Patente US1310719-A de 1919 por Gilbert S. Vernam

ATENÇÃO: esta é uma cifra facilmente quebrada analisando a frequência
dos bytes quando a chave é menor que o conteúdo. Deve ser usada apenas
para esconder informações contra leitura acidental.
"""

from array import array

CODIFICACAO_DEFAULT = 'utf-8'

def vernam(chave, conteudo):
    """cifra XOR de G. S. Vernam

    Argumentos:
    chave -- bytes da chave
    conteudo -- bytes do texto

    Resultado:
    bytes com o conteudo cifrado
    """
    saida = array('B', conteudo)
    for i, byte in enumerate(conteudo):
        saida[i] = byte ^ chave[i % len(chave)]
    return saida

def string_para_bytes(string, codificacao):
    if type(string) is unicode:
        string = string.encode(codificacao)
    return array('B', (ord(c) for c in string))

def main():
    import sys
    from getpass import getpass
    if len(sys.argv) != 2:
        print('Modo de usar: xor.py <nome_arquivo>')
        sys.exit()
    chave = getpass('Senha:').encode(CODIFICACAO_DEFAULT)
    nome_entrada = sys.argv[1]
    if nome_entrada.endswith('.blob'):
        nome_saida = nome_entrada + '.txt'
    else:
        nome_saida =  nome_entrada + '.blob'
    with open(nome_entrada, 'rb') as entrada:
        conteudo = entrada.read()
    if sys.version_info.major == 2:  # Python 2
        chave = string_para_bytes(chave, CODIFICACAO_DEFAULT)
        conteudo = string_para_bytes(conteudo, CODIFICACAO_DEFAULT)        
    with open(nome_saida, 'wb') as saida:
        saida.write(vernam(chave, conteudo))
    print('%d bytes escritos em %s' % (len(conteudo), nome_saida))

if __name__=='__main__':
    main()
