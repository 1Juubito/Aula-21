palavras = ('Mario', 'Luigi', 'Yoshi', 'Peach', 'Bowser')
for palavra in palavras:
    print(f'\nPalavra: {palavra.upper()}. Vogais: ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')