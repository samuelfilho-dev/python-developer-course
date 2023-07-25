def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def exibir_resultados(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O Resultado Da Operação {a} + {b} = {resultado}")


exibir_resultados(10, 10, somar)  # O Resultado Da Operação 10 + 10 = 20
exibir_resultados(10, 10, subtrair)  # O Resultado Da Operação 10 - 10 = 0

# Passar funcao como varivavel
op = somar
print(op(1, 23))
