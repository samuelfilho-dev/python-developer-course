# texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

# For - Que Pecorre um Objeto Iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # Adiciona uma quebra de Linha
    print("Execulta Final De Laço")

# For - Que Pecorre atraves da Função Range
for numero in range(0, 51, 5):
    print(numero, end=" ")
