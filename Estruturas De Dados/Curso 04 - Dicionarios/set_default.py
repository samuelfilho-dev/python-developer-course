contato = {"nome": "Samuel", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # Samuel
print(contato)  # {'nome': 'Samuel', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Samuel', 'telefone': '3333-2221', 'idade': 28}
