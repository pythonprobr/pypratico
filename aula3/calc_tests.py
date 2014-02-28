# -*- coding: utf-8 -*-
import unittest


def somar(param1, param2):
    return param1 + param2


def maior_q_5(numero):
    return numero > 5


class CalculadoraTests(unittest.TestCase):
    def test_funcao_somar(self):
        resultado = somar(1, 2)
        self.assertEqual(3, resultado)
        resultado = somar(3, 2)
        self.assertEqual(5, resultado)


    def test_maior_q_5(self):
        resultado = maior_q_5(-50000)
        self.assertFalse(resultado)
        self.assertFalse(maior_q_5(4))
        self.assertFalse(maior_q_5(5))
        self.assertTrue(maior_q_5(6))
        self.assertTrue(maior_q_5(600000))


if __name__ == '__main__':
    # unittest.main()
    class Pessoa():
        def __init__(self, nome):
            self.nome = nome

        def ola(self):
            return "Olá %s" % self.nome

    renzo = Pessoa('Renzo')
    leonardo = Pessoa('Leonardo')

    print(renzo.ola())
    print(leonardo.ola())