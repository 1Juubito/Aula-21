#mesma referência
lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original
print(lista_original)
print(lista_referenciada)

lista_referenciada[0] = 2
print(lista_original)
print(lista_referenciada)

#cópia

lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original[:]
print(lista_original)
print(lista_referenciada)

lista_referenciada[0] = 2
print(lista_original)
print(lista_referenciada)

