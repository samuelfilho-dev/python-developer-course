def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


def func_3():
    print("Hello World")


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_sucessor(10))  # (9, 11)
print(func_3())  # None
