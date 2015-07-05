
.. Python Prático slides file, created by
   hieroglyph-quickstart on Sun Jul  5 01:16:08 2015.

==============
Python Prático
==============


Em vez de "Hello, World!"
=========================

Gerador de senhas aleatórias. Versão Twitter:

.. literalinclude:: ../cifras/senha_tweet.py
    :caption:


Versão `PEP-8 <https://www.python.org/dev/peps/pep-0008/>`_:


.. literalinclude:: ../cifras/senha_pep8.py
    :caption:


Gerando bytes aleatórios
========================

``os.urandom(n)``
    Devolve uma sequência de n bytes aleatórios apropriados para uso criptográfico.

.. code-block:: python
    :caption: Experimente no console do Python 3:

    >>> import os
    >>> octetos = os.urandom(9)
    >>> octetos
    b'\xe9NHor.\xd0\x05\x96'
    >>> len(octetos)
    9
    >>> octetos = os.urandom(9)
    >>> octetos
    b'Z6\xe1\xa4W\x06\xbe\xa0\xce'
    >>> len(octetos)
    9
    >>> type(octetos)
    <class 'bytes'>


Bytes versus texto humano no Python 3
=====================================

No Python 3, o tipo ``str`` serve para strings de texto humano (Unicode), e o tipo ``bytes`` serve para bytes.

Exemplos::

    >>> texto = 'avião'
    >>> type(texto)
    <class 'str'>
    >>> octetos = texto.encode('utf8')
    >>> octetos  # repare no prefixo b''
    b'avi\xc3\xa3o'
    >>> type(octetos)
    <class 'bytes'>
    >>> len(texto), len(octetos)
    (5, 6)
    >>> bytes is str
    False


Bytes versus texto humano no Python 2.7
=======================================

No Python 2.7, o tipo ``unicode`` serve para strings de texto humano (Unicode), e o tipo ``str`` serve para bytes. Também existe o tipo ``bytes``, mas é apenas um sinônimo de ``str``.

Exemplos::

    >>> texto = u'avião'  # repare no prefixo: u''
    >>> type(texto)
    <type 'unicode'>
    >>> octetos = texto.encode('utf8')
    >>> octetos
    'avi\xc3\xa3o'
    >>> type(octetos)
    <type 'str'>
    >>> len(texto), len(octetos)
    (5, 6)
    >>> bytes is str
    True


Conversão entre texto e bytes no Python 3
==========================================

No Python 3, o método ``str.encode()`` devolve bytes::

    >>> texto = u'avião'  # prefixo opcional no 3.4
    >>> texto.encode('utf8')  # bytes na codificação UTF-8
    b'avi\xc3\xa3o'
    >>> texto.encode('cp1252')  # Windows codepage 1252
    b'avi\xe3o'

E o método ``bytes.decode()`` devolve texto Unicode::

    >>> octetos = b'avi\xc6o'
    >>> print(octetos)
    b'avi\xc6o'
    >>> octetos.decode('cp850')  # MS/DOS codepage 850
    'avião'
    >>> print(octetos.decode('cp850'))
    avião


Conversão entre texto e bytes no Python 2.7
===========================================

No Python 2.7, o método ``unicode.encode()`` devolve bytes (``str``)::

    >>> texto = u'avião'
    >>> texto.encode('utf8')  # bytes na codificação UTF-8
    'avi\xc3\xa3o'
    >>> texto.encode('cp1252')  # Windows codepage 1252
    'avi\xe3o'

E o método ``bytes.decode()`` devolve texto Unicode::

    >>> octetos = b'avi\xc6o'  # prefixo opcional no 2.7
    >>> print(octetos)
    avi�o
    >>> octetos.decode('cp850')  # MS/DOS codepage 850
    u'avi\xe3o'
    >>> print(octetos.decode('cp850'))
    avião

