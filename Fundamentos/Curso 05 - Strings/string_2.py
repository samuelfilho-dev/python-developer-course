nome = "Samuel"
idade = 21
profissao = "Garoto de Programa"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Samuel", "idade": 21}

# Old Style - Formatação Antiga
print("Nome: %s Idade: %d" % (nome, idade))

# Metodo Format
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))  # Pode passar os Indices no '{}'
print("Nome: {1} {1} {1}".format(idade, nome))  # Pode repitir mais facil as varivaveis com passar dos indices
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))  # Pode passar como args no '{}'
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade,
                                                             name=nome))  # Tem os mesmos beneficios dos indices
print("Nome: {nome} Idade: {idade}".format(**dados))  # Utilização de Dicionarios

# F-String
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}") # Formatação De Float na F-string
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}") 

