''' Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores. '''

from datetime import date
ano_atual = date.today().year
ano = 0
maiores_idade = 0
menores_idade = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    idade_pessoa = ano_atual - ano

    if idade_pessoa > 18:
        maiores_idade = maiores_idade + 1
    else:
        menores_idade = menores_idade + 1
print(''
      '')
print('{} pessoas maiores de idade e {} pessoas menores de idade'.format(maiores_idade,menores_idade))

