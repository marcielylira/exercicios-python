'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

genero= str(input('Digite o genero [M,F]: ')).strip().upper()[0]
while genero not in 'FM':
    genero= str(input('Resposta inválida. Digite novamente: ')).strip().upper()[0]
print('Informação registrada com sucesso!')


