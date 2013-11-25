# coding: utf-8

import unittest
import array

import xor

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.conteudo_bytes = array.array('B', range(256))
        self.senha_bytes = [0, 42, 255]

    def test_vernam(self):
        self.assertEqual(
            xor.vernam(self.senha_bytes,
                xor.vernam(self.senha_bytes, self.conteudo_bytes)),
            self.conteudo_bytes)

if __name__ == '__main__':
    unittest.main()
