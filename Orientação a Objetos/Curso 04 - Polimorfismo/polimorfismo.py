class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal Pode Voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz Não Pode Voar")


# FIXME: Exemplo ruim do uso de herança, Para Herdar o Metodo Voar
class Aviao(Passaro):
    def voar(self):
        print("Avião Está Decolando")


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
