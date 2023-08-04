"""
 - Comentarios
    - Primeira Letra do comentario deve ser Maiúscula
    - Comentario de uma linha não deve ter espaçamento
 - DocStrings
    - Se cria uma Doc string usando """ """ ou ''' '''
    -  Docstring no topo do arquivo
        - Tem copyrights
        - Nome do autores
        - Objetivos do Módulo o biblioteca
    - Docstring dentro do métodos
        - Tem objetivo do metodo
        - Tem os parametros
        - Tem o retorno do metodo
"""


class Persona:
    def __init__(self, message):
        self.name = None
        self.email = None
        self.inicio = message

    def set_name(self, name):
        """
        Esté método tem como objetivo setar
        o nome do Objeto instanciado pela classe

        :param name: nome definido pelo usuario
        :return: self.name
        """
        self.name = name
        print('O nome é: ', name)
        return self.name


p1 = Persona("Olá")
p1.set_name("Juliana")  # O docstring aparece como pop-up nas IDE


def retorno_funcao_args(arg_one, arg_two,
                        arg_three, arg_four):
    # Comentario de uma linha
    return (arg_one + arg_two) / (arg_three + arg_four)



