"""
 Exemplo para utilizando do Pylint como linter. Assim podemos verificar
 a validação da PEP 8.

 Como habilitar o pylint no pycharm
 file -> settings -> plugins -> pylint
"""
import pandas, numpy
import pandas as pd


def funcao(parametro):
    x = 2
    y = x + 3
    z = 8
    return x * z


funcao(8)
