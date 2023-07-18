contatos = {
    "guilerme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "meliane@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}
}

# 1ª Forma de Iteração
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

# 2ª Forma de Iteração
for chave, valor in contatos.items():
    print(chave, valor)
