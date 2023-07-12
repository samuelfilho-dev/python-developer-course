saldo = 2000
saque = 2500

# If Ternario - <Bloco De Código De Sucesso> if <Condição> else <Bloco De Código De Falha>
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao Realizar o Saque")
