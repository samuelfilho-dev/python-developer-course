"""
 - na PEP 8, define 4 espaços como indentação no código
 - Crtl + Alt + L, Organiza a identação do código
 - Espaços define final de comando no Python
 - Não é legivel colocar módulos em uma liha separado por virgula
 - Ordem de importação de Módulos no python
    - 1ª: Módulos já instalado no Python
    - 2ª: Módulos que foram instalados pelo PIP
    - 3ª: Módulos específicos: extrai somente funções e/ou classe
        - from <caminho> import <(Função, Classe)>
"""
# Errado
import sys, os

import pandas
import matplotlib
import numpy

from pandas import array

# var = 1 var2 = 2 # Errado
var = 1
var2 = 2


# Outra forma de definir argumentos de uma função
def retorno_funcao_args(arg_one,
                        arg_two,
                        arg_three,
                        arg_four, ):
    pass
