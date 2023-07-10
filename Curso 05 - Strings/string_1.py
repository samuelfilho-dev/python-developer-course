# Maisculo e Minusculo
nome = "sAmUeL"

print(nome.upper())  # Coloca a String em Maisculo
print(nome.lower())  # Coloca a String em Minusculo
print(nome.title())  # Coloca a primeira letra da String em Maisculo

# Remoção do Espaços
texto = "     Olá Mundo             "

print(texto)
print(texto.strip() + ".")  # Elimina todos os espaços
print(texto.rstrip() + ".")  # Elimina o espaço da direita
print(texto.lstrip() + ".")  # Elimina o espaço da esquerda

# Junção e Centralização
menu = "Python"

print("####" + menu + "####")
print(menu.center(20, "#")) # Centralizar uma String
print("P-y-t-h-o-n")
print("-".join(menu))
