# Operadores Logicos
# Operador "E" - Para ser Verdadeiro - Todas as senteças precisam ser verdadeiras
# Operador "OU" - Para ser Verdadeiro - Apenas uma setença precisa ser verdadeiras
print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Expressão 1
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

# Expressão 2
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

# Pode Quebrar as expressões Booleanas para melhor compreensão
conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

# Expressão 3
exp3 = conta_especial_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp3)
