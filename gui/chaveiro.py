#!/usr/bin/env python3

"""

A Classe chaveiro é uma interface de alto nível para ler e gravar arquivos
cifrados contendo listas de chaves.

    >>> from chaveiro import Chaveiro
    >>> chaves = Chaveiro('1234')
    >>> chaves.ler()
    >>> len(chaves)
    47
    >>> chaves[:3]  #doctest: +NORMALIZE_WHITESPACE
    [['Learn Chinese Characters', 'http://zhongwen.com/', 'admin', 'l>:&=+'],
     ['famfamfam.com: Home', 'http://www.famfamfam.com/', 'lramalho', 'y=SCKu'],
     ['G-Portugol', 'http://gpt.berlios.de/', 'lramalho', 'z&>45']]

Cada chave é formada por 4 atributos: título, endereço, login e senha:

    >>> chaves[10]  #doctest: +NORMALIZE_WHITESPACE
    ['The Public DNS Service', 'http://soa.granitecanyon.com/',
     'lramalho', 'awxn:t0']

"""

import pickle
import zlib
from os import urandom, rename, remove

from hashlib import sha1 # Python 2.5.x

from rc4 import rc4

NOME_ARQ_PADRAO = 'chaveiro.dat'
FORMATO_PICKLE = 2
CODIF = 'utf-8'

def cifrar(senha, octetos):
    ''' Cifrar octetos usando algoritmo RC4 como no Ciphersaber 2

    O Ciphersaber 2 usa um vetor inicial de 10 octetos aleatórios concatenado
    à senha do usuário, e 20 iterações no laço de inicialização do RC4.

    fonte: http://ciphersaber.gurus.com/faq.html#cs2
    '''
    vetor_inicial = urandom(10)
    senha = bytes(senha, CODIF) + vetor_inicial
    return vetor_inicial + rc4(senha, octetos, 20)

def decifrar(senha, octetos):
    ''' Decifrar octetos usando algoritmo RC4 como no Ciphersaber 2 '''
    senha = bytes(senha, CODIF) + octetos[:10]
    octetos = octetos[10:]
    return rc4(senha, octetos, 20)

class SenhaIncorreta(Exception):
    "Senha-mestre incorreta."

class ArquivoCorrompido(Exception):
    "Arquivo de dados corrompido."

class Chaveiro(object):
    ''' Gerencia uma lista de chaves

    A lista de chaves pode ser gravada ou lida num arquivo cifrado em RC4.

    Para maior segurança contra falhas, ao gravar os dados cifrados, o programa
    salva os dados em um arquivo .NEW, renomeia o arquivo atual para .BKP e só
    então retira o sufixo .NEW e apaga o arquivo .BKP. O arquivo gravado inclui
    um hash SHA-1 que permite verificar sua integridade na leitura.
    '''

    def __init__(self, senha, nome_arq=NOME_ARQ_PADRAO):
        self.senha = senha
        self.nome_arq = nome_arq
        self.chaves = []

    def __iter__(self):
        for chave in self.chaves:
            yield chave

    def __len__(self):
        return len(self.chaves)

    def __getitem__(self, indice):
        return self.chaves[indice]

    def incluir(self, chave, posicao=None):
        if posicao is None:
            self.chaves.append(chave)
        else:
            self.chaves.insert(posicao, chave)

    def excluir(self, posicao):
        del self.chaves[posicao]

    def carregar(self, chaves, sobrescrever=True):
        if sobrescrever:
            self.chaves = chaves
        else:
            self.chaves.extend(chaves)

    def gravar(self):
        arq = open(self.nome_arq+'.NEW','wb')
        octetos = pickle.dumps(self.chaves, FORMATO_PICKLE)
        octetos = zlib.compress(octetos)
        octetos = cifrar(self.senha, octetos)
        assinatura = sha1(octetos).digest()
        arq.write(assinatura)
        arq.write(octetos)
        arq.close()
        try:
            rename(self.nome_arq, self.nome_arq+'.BKP')
        except OSError as erro:
            if 'No such file or directory' in str(erro):
                apagar_backup = False
            else:
                raise erro
        else:
            apagar_backup = True
        rename(self.nome_arq+'.NEW', self.nome_arq)
        if apagar_backup:
            remove(self.nome_arq+'.BKP')

    def ler(self):
        arq = open(self.nome_arq,'rb')
        verificador = sha1()
        assinatura = arq.read(verificador.digest_size)
        octetos = arq.read()
        arq.close()
        verificador.update(octetos)
        if assinatura != verificador.digest():
            raise ArquivoCorrompido()
        octetos = decifrar(self.senha, octetos)
        try:
            octetos = zlib.decompress(octetos)
        except zlib.error as erro:
            raise SenhaIncorreta()
        else:
            self.chaves = pickle.loads(octetos, encoding=CODIF)

if __name__ == "__main__":
    import doctest
    res = doctest.testmod()
    if res.failed == 0:
        print('OK.', res)
    else:
        print('FALHAS!', res)
