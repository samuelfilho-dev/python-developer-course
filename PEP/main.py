"""
- Nomear Funções:
    - sem '_' no espaços das palavras, 'Explicito'
    - Colocar paramentros condizente com a sua finalidade
    - Todas os nomes de funções são em minusculas - uppercase
    - Separação de parametro de funções deve seguir a identação:
            (arg_one, arg_two,
            arg_three, arg_four):
- Nomer Classes
    - Começam com letra maiúscula
    - Estilo de nomeação da Classe é 'CamelCase', Ex: class JuridicPerson
    - Dois espaços em branco pós declaração da classe
    - 'self' como inicio de metodos na classes
    - Métodos são separados por '_', da mesma forma que função
- Nomear Variváveis
    - Não colocar caracteres especiais
    - Um espaço entre o nome, simbolo de atribuição, valor da variavel
- Nomear Constantes
    - São nomeadas em letras Maiúscula - UPPERCASE
- Nomear Comentario
    - Dois espaços para colocar um comentario em uma linha de codigo
"""

# Constantes
CONSTANT = 100


class Persona:
    def __init__(self, message):
        self.name = None
        self.email = None
        self.inicio = message

    def set_name(self, name):
        self.name = name
        print('O nome é: ', name)


variveis = 0
x =1  # Errado
y=2  # Errado

number_one = 1


def retorno_funcao_args(arg_one, arg_two,
                        arg_three, arg_four):
    pass


# Errado
def retornofuncaoargs(
        arg_one, arg_two,
        arg_three, arg_four):
    pass


def print_hi_with_message(name):
    print(f"Hi, {name}")


def printhiwithmessage(name):  # Errado
    pass


def function_x(x, y, z):  # Errado
    t = (x + y) / z
    pass


def media_aluno(nota1, nota2, divisor):
    t = (nota1 / nota2) / divisor
    pass
