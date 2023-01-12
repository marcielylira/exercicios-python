'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num= (int(input('Digite um número: ')))
total= 0

for c in range (1, num + 1):
    if num % c == 0:
        total= total + 1
if total == 2:
    print('NÚMERO PRIMO')
else:
    print('NÃO É PRIMO')

