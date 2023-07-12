conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

# Exemplo de If Aninhado
if conta_normal:
    if saldo >= saque:
        print("Saque Realizado Com Sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saldo Realizado Pelo Cheque Especial")
    else:
        print("Não Foi Possivel Realizar o Saque, Saldo Insuficiente")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque Realizado Com Sucesso")
    else:
        print("Saldo Insuficiente")

elif conta_especial:
    print("Conta Especial Selecionada")

else:
    print("O Sistema não reconhece seu tipo de Conta, entre em contato com o seu Gerente")
