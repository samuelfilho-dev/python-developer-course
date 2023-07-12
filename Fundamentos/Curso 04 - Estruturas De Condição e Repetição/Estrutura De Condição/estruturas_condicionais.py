MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a Sua Idade: "))

# Condição Simples
if idade >= MAIOR_IDADE:
    print("Maior de Idade, Pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")

# Condição - If...Else
if idade >= MAIOR_IDADE:
    print("Maior de Idade, Pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")

# Condição - If...Elif...Else
if idade >= MAIOR_IDADE:
    print("Maior de Idade, Pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode Fazer Aulas Teoricas, Mas Não Pode fazer Aulas Praticas")
else:
    print("Ainda não pode tirar a CNH")
