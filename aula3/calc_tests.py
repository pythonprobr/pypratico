# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock


class Soma():
    sinal = '+'

    def calcular(self, param1, param2):
        return param1 + param2


class OperacaoTests(unittest.TestCase):
    def test_operacao_somar(self):
        operacao = Soma()
        self.assertEqual('+', operacao.sinal)
        resultado = operacao.calcular(3, 2)
        self.assertEqual(5, resultado)


class Calculadora(object):
    def __init__(self):
        self._operacoes = {}
        self.sinal_escolhido = None

    def incluir_operacao(self, operacao):
        self._operacoes[operacao.sinal] = operacao

    def calcular(self, param, param1):
        operacao = self._operacoes[self.sinal_escolhido]
        return operacao.calcular(param, param1)


class CalculadoraTests(unittest.TestCase):
    def test_incluir_operacao(self):
        calculadora = Calculadora()
        self.assertDictEqual({}, calculadora._operacoes)
        operacao = Soma()
        calculadora.incluir_operacao(operacao)
        self.assertDictEqual({'+': operacao}, calculadora._operacoes)

    def test_calcular(self):
        calculadora = Calculadora()
        SINAL_ESCOLHIDO = '#'
        RESULTADO_ESPERADO = 8

        # class OperacaoMock():
        #     sinal = SINAL_ESCOLHIDO
        #
        #     def calcular(self, param, param2):
        #         self.param = param
        #         self.param2 = param2
        #         return RESULTADO_ESPERADO

        mock = Mock()
        calculadora.sinal_escolhido = SINAL_ESCOLHIDO
        mock.sinal = SINAL_ESCOLHIDO
        mock.calcular = Mock(return_value=RESULTADO_ESPERADO)

        calculadora.incluir_operacao(mock)
        resultado = calculadora.calcular(2, 3)
        self.assertEqual(RESULTADO_ESPERADO, resultado)
        mock.calcular.assert_called_once_with(2, 3)

        # mock.um_metodo(4, 5, 'blah')
        # mock.um_metodo(4, 5, 'blah')
        # mock.um_metodo.assert_called_once_with(4, 5, 'blah')


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