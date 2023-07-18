contatos = {"guilerme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilerme@gmail.com")
print(resultado)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

resultado = contatos.pop("guilerme@gmail.com", {}) # Colocar o valor padrão, caso não encontre a chave
print(resultado)  # {}
