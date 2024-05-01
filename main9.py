#Trabalhando com métodos em strings

s1 = list('Algoritmos')
print(s1) #print separado
print(''.join(s1)) #print agrupado

s1[0] = 'a'
print(''.join(s1))

#Verificando caracteres


s1 = 'Lógica de Programação e Algoritmos'
s1.startswith('Lógica') #True
s1.endswith('Algoritmos') #True

s1 = 'Lógica de Programação e Algoritmos'
s1.lower().endswith('algortimos')

s1 = 'Lógica de Programação e Algoritmos'
print(s1.upper())
print(s1.lower())

#contando caracteres

s1 = 'Lógica de Programação e Algoritmos'
s1.count('a')

s1 = 'Lógica de Programação e Algoritmos'
s1.lower().count('a')

s1 = 'Um mafagafinho, dois mafagafinhos, três mafagafinhos...'
s1.lower().count('mafagafinho')


s1 = 'Lógica de Programação e Algoritmos'
s1.split(' ')

s1 = 'Um mafagafinho, dois mafagafinhos, três mafagafinhos...'
s1.replace('mafagafinho', 'gatinho',1)


