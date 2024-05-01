cadastro = {'nome': [], 'sexo': [], 'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar.upper() == 'N':
        break
    elif terminar.upper() not in 'S':
        print('Digite S para SIM e N para NÃO.')
        continue

    nome = input('Digite o nome: ')
    sexo = input('Digite o sexo: ')
    ano = int(input('Digite o ano de nascimento: '))


    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo)
    cadastro['ano'].append(ano)

print(cadastro)
total_cadastros = 0
for i in cadastro['nome']:
    total_cadastros += 1
print(f'Total de cadastros: {total_cadastros}')

idades = [2024 - int(ano) for ano in cadastro['ano']]
media_idades = sum(idades) / total_cadastros
print(f'Média das idades: {media_idades:.2f}')

mulheres_menos_30 = [cadastro['nome'][i] for i in range(total_cadastros) if cadastro['sexo'][i] == 'F' and idades[i] < 30]
homens_acima_media = [cadastro['nome'][i] for i in range(total_cadastros) if cadastro['sexo'][i] == 'M' and idades[i] > media_idades]

print(f'Mulheres com menos de 30 anos: {mulheres_menos_30}')
print(f'Homens com idade acima da média: {homens_acima_media}')
