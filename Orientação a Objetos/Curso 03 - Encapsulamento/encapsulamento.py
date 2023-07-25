class Conta:
    def __init__(self, saldo, nro_agencia):
        self._saldo = saldo  # _<Atributo> Atributo Privado por conveção no Python
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ....
        self._saldo -= valor

    def consultar_saldo(self):
        return self._saldo


conta = Conta(100, "0001")
conta.depositar(100)
print(conta.nro_agencia)

print(conta._saldo)  # Acesso Não Permitido
print(conta.consultar_saldo())  # Acesso Permitido
