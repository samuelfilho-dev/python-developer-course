"""
 - Deve haver um espaçamento entre a declaração da funcão e o resto do codigo
    - Minimo: 2 espaço
 - Deve haver um espaçamento nas estrutura de dados
 - Deve haver um espaçamento nos paramentros das funções
 - Deve haver um espaçamento entre as estuturas condicionais conversionais do Python
 - Não deve haver um espaçamento na virgula final da tupla
"""


def media_aluno(nota1, nota2, divisor):
    t = (nota1 + nota2) / divisor
    pass


def funcao_ficiticia(*args):
    pass


media_aluno(5, 9, 2)
media_aluno(7, 9, 2)
vetor = []
x = 0
y = 0

funcao_ficiticia(vetor[1,2,3], {'key':2}) # Errado
funcao_ficiticia(vetor[1, 2, 3], {'key': 2})

if x==4: print(x,y); x,y=y,x # Errado

# Correta
if x == 4:
    print(x, y)
    x, y = y, x

foo = (0,)  # Correto
bar = (0, )  # Errado
