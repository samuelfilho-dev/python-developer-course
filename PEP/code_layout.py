"""
 - Tamanho maximo: 79 caracteres por linha
 - Importações
    - Importar bibliotecas diferentes, não usa mesmo import
    - Puxando Módulo de uma biblioteca usa:
        - from <Biblioteca> import <Clase>
    - Puxando mais de um Módulo na biblioeteca usa:
    - Quebra de mútiplas linhas
        - from <Biblioteca> import (
            - <Classes>
        )
 - Listas e Matriz
    - Na criação de Lista ou Matrizes deve haver a criação de espaçamentos e quebra de linha
"""

import matplotlib
import numpy
import pandas

from pandas import array
from pandas import (
    Series,
    read_csv,
    DataFrame,
    HDFStore
)

lista = [1,2,3,4,5,6,7,8,9]  # Errado com relação a espaçamento e disposição
matriz = [1, 2, 3,
          4, 5, 6,
          7, 8, 9
          ]
