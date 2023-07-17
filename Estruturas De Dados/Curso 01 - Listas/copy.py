lista = [1, "python", [40, 30, 20]]

l2 = lista.copy()  # Instancia a lista em outro endereço de memoria

print(lista)  # [1, "python", [40, 30, 20]]
print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)
