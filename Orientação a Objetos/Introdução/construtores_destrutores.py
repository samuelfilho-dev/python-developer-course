class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a Classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instancia da Classe")

    def falar(self):
        print("Au Au Au")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e Preto", False)
    print(c.nome)


c = Cachorro("Chappie", "Amarelo")
c.falar()

criar_cachorro()
