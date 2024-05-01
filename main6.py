item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: '))
    item.append(int(input('Digite a quantiadade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])
    item.clear()
print(mercado)

# Mesmo resultado

mercado = []

for i in range(3):
    nome = input('Digite o nome do item: ')
    qtd = int(input('Digite a quantiadade: '))
    valor = float(input('Digite o valor: '))
    mercado.append([nome, qtd, valor])

soma = 0
print('Lista de compras: ')
print('-' * 20)
print('Item | quantidade | valor unitário | total do item')
for item in mercado:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print(f'Total a ser pago: {soma:.2f}')

