'''
Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo,
desconsiderando os espaços. :
'''

frase = str(input('Digite uma frase: ')).strip().upper()

separação = frase.split()
junto = ''.join(separação)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso != junto:
    print('A frase não é um Palíndromo')
else:
    print('A frase é um Palíndromo')