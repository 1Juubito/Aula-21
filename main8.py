#Lista com dicionários

games = []
game1 = {'Nome': 'Super Mario',
        'VideoGame': 'Super Nintendo',
        'Ano': 1990}
game2 = {'Nome': 'Zelda Ocarina of Time',
        'VideoGame': 'Nintendo 64',
        'Ano': 1998}
game3 = {'Nome': 'Pokemon Yellow',
        'VideoGame': 'Game Boy',
        'Ano': 1999}
games = [game1, game2, game3]
print(games)



game = {}
games = []

for i in range(3):
    game['Nome'] = input('Digite o nome do jogo: ')
    game['VideoGame'] = input('Digite o nome do videogame: ')
    game['Ano'] = int(input('Digite o ano de lançamento: '))
    games.append(game.copy())
print('-' * 20)
for jogos in games:
    for chave, valor in jogos.items():
        print(f'O campo {chave} tem o valor {valor}.')


#Dicionário com listas

games = {'nome': ['Super Mario', ' Zelda Ocarina of Time', 'Pokemon Yellow'],
        'videogame': ['Super Nintendo', 'Nintendo 64', 'Game Boy'],
        'ano': [1990, 1998, 1999]}
print(games)


games = {'nome': [], 'videogame': [], 'ano': []}
for i in range (3):
    nome = input('Qual o nome do jogo?')
    videogame = input('Para qual video game ele foi lançado?')
    ano = input('Qual o ano de lançamento?')
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)


