mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

print(mochila[-1]) #Acessando item dentro da mochila

for item in mochila:
    print(f'Na minha mochila tem: {item}')



tam = len(mochila)
for i in range (0, tam, 1):
    print(f'Na minha mochila tem: {mochila[i]}')



mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochilaUpgrade = mochila + upgrade
print(mochila)
print(upgrade)
print(mochilaUpgrade)



