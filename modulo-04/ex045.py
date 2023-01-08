'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep

itens= ('PEDRA', 'PAPEL', 'TESOURA')
comp= randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
usuario= int(input('Qual é a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('O computador escolheu: {}'.format(itens[comp]))
print('O usuário escolheu: {}'.format(itens[usuario]))

if comp == 0:
    if usuario == 0:
        print('EMPATE!')
    elif usuario == 1:
        print('USUÁRIO GANHOU!')
    elif usuario == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('\033[32mJOGADA INVÁLIDA!')
elif comp == 1:
    if usuario == 0:
        print('COMPUTADOR GANHOU!')
    elif usuario == 1:
        print('EMPATE!')
    elif usuario == 2:
        print('USUÁRIO GANHOU!')
    else:
        print('\033[32mJOGADA INVÁLIDA!')
elif comp == 2:
    if usuario == 0:
        print('USUÁRIO GANHOU!')
    elif usuario == 1:
        print('COMPUTADOR GANHOU!')
    elif usuario == 2:
        print('EMPATE!')
    else:
        print('\033[32mJOGADA INVÁLIDA')
else:
    print('JOGADA INVÁLIDA')
