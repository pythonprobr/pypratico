# -*- coding: utf-8 -*-


import unittest
from unittest.mock import Mock


class Soma():
    sinal = '+'

    def calcular(self, param, param1):
        return param + param1


class TestOperacao(unittest.TestCase):
    def test_soma(self):
        soma = Soma()
        self.assertEqual('+', soma.sinal)
        self.assertEqual(4, soma.calcular(2, 2))
        self.assertAlmostEqual(3.14, soma.calcular(1, 2.14), delta=0.00001)


class Calculadora():
    def __init__(self):
        self._operacoes = {}
        self.operacao_atual = None

    def adicionar_operacao(self, operacao):
        self._operacoes[operacao.sinal] = operacao

    def calcular(self, arg1, arg2):
        return self._operacoes[self.operacao_atual].calcular(arg1, arg2)


class TestCalculadora(unittest.TestCase):
    def test_adicelionar_operacao(self):
        calculadora = Calculadora()
        self.assertDictEqual({}, calculadora._operacoes)
        operacao = Mock()
        operacao.sinal = '#'
        calculadora.adicionar_operacao(operacao)
        self.assertDictEqual({'#': operacao}, calculadora._operacoes)

    def test_calcular(self):
        calculadora = Calculadora()
        operacao = Mock()
        operacao.sinal = '#'
        operacao.calcular = Mock(return_value=8)
        calculadora.adicionar_operacao(operacao)
        calculadora.operacao_atual = '#'
        resultado = calculadora.calcular(2, 3)
        self.assertEqual(8, resultado)
        operacao.calcular.assert_called_once_with(2, 3)