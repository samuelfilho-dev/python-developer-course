class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod  # Metodo De Classe - Usado para criar novas intancias da classe
    def criar_apartir_data_nascimeto(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return cls(nome, idade)  # Por convesão, usamos 'cls' para representar a instancia da classe

    @staticmethod
    def e_maior_de_idade(idade):  # Metodo Estatico - Não usa a instancia da classe, objeto
        return idade >= 18


p = Pessoa("Samuel", 21)
print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimeto(2001, 3, 21, "Samuel")
print(p.nome, p.idade)

print(Pessoa.e_maior_de_idade(18))
print(Pessoa.e_maior_de_idade(8))
