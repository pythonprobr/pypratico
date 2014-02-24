

import unittest
from cp850_data import cp850_high

from demo_codif_stdout import gerar_amostra, associar_nomes, codificar_amostra


class TestarGerarAmostra(unittest.TestCase):

    def setUp(self):
        self.ABC = list('ABC')
        self.latin1 = [chr(i) for i in range(32, 256)]
        self.cp850 = ([chr(i) for i in range(32, 128)] +
                      [chr(i) for i in cp850_high])

    def teste_gerar_latin1(self):
        amostra = gerar_amostra('iso8859-1')
        self.assertEqual(amostra, self.latin1)

    def teste_gerar_cp850(self):
        amostra = gerar_amostra('cp850')
        self.assertEqual(amostra, self.cp850)

    def teste_associar_nomes_existentes(self):
        pares = associar_nomes(self.latin1)
        de_para = dict(pares)
        self.assertEqual(de_para['A'], 'LATIN CAPITAL LETTER A')
        self.assertEqual(de_para['ÿ'], 'LATIN SMALL LETTER Y WITH DIAERESIS')
        self.assertEqual(de_para['ã'], 'LATIN SMALL LETTER A WITH TILDE')

    def teste_associar_nomes_inexistentes(self):
        pares = associar_nomes(self.latin1)
        de_para = dict(pares)
        self.assertEqual(de_para['\x7f'], '<no such name>')
        self.assertEqual(de_para['\x80'], '<no such name>')

    def teste_codificar_amostra_ABC(self):
        codificada = codificar_amostra(self.ABC, 'ascii')
        self.assertEqual([b'A', b'B', b'C'], codificada)

    def teste_codificar_amostra_compativel(self):
        """
        a1 ¡ INVERTED EXCLAMATION MARK
        a2 ¢ CENT SIGN
        a3 £ POUND SIGN
        """
        codificada = codificar_amostra(self.latin1, 'iso8859-1')
        self.assertEqual([b'\xa1', b'\xa2', b'\xa3'], codificada[161-32:164-32])

    def teste_codificar_amostra_incompativel(self):
        """
        80 <undefined>
        """
        codificada = codificar_amostra(self.latin1, 'cp437', b'!')
        self.assertEqual(b'!', codificada[128-32])


    def teste_codificar_amostra_cp850(self):
        """
        0xa0 0x00e1 á LATIN SMALL LETTER A WITH ACUTE
        0xe6 0x00b5 µ MICRO SIGN
        """

if __name__ == '__main__':
    unittest.main()
