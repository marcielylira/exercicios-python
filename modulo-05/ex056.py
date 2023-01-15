'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

soma = 0
media = 0
mulheres = 0
maior = 0
mais_velho = ''

for cont in range(1,5):
    nome = input('Nome: ')
    sexo = input('Sexo [M/F]: ').upper()[0]
    idade = int(input('Idade : '))
    print('-'*20)

    soma = soma + idade
    media = soma / cont

    if sexo == 'M' and idade > maior:
        maior = idade
        mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
print('A média de idade é de {:.2f} '.format(media))
print('O homem mais velho é o {}'.format(mais_velho))

if mulheres == 0:
    print('Não tem mulheres no grupo !')
else:
    print('A todo são {} mulheres com menos de 20 anos'.format(mulheres))