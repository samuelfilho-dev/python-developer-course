from abc import ABC, abstractmethod, abstractproperty  # Importa o modulo que define classe abstrata


class ControleRemoto(ABC):  # Classe Abastrata - Interface

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):

    def ligar(self):
        print("Ligando a TV")
        print("Ligada")

    def desligar(self):
        print("Desligando a TV")
        print("Desligada")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):

    def ligar(self):
        print("Ligando o Ar-Condicionado")
        print("Ligado")

    def desligar(self):
        print("Desligando o Ar-Condicionado")
        print("Desligando")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)
