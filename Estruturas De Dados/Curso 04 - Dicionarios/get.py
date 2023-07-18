contatos = {"guilerme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# 1ª Forma
resultado = contatos.get("chave")
print(resultado)  # None

# 2ª Forma
resultado = contatos.get("chave", {})
print(resultado)  # {}

# 3ª Forma
resultado = contatos.get("guilerme@gmail.com", {})
print(resultado)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contatos["chave"]  # KeyError
