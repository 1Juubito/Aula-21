mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0][0]) #String dentro de string


mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for item in mochila:
    for letra in item:
        print(letra, end=' ')
    print()


mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for i in range(0, len(mochila),1):
    for j in range(0, len(mochila[i]),1):
        print(mochila[i][j], end='')
    print()


# lista dentro de lista

mochila = [['Cebola', 0.39], ['Tomate', 0.49], ['Maçã', 0.89]]
print(mochila[0][0][0]) #Tripla
print(mochila[2][1]) #Dupla

