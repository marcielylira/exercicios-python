#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
num= int(input('TENTE ADIVINHAR O NÚMERO SORTEADO ENTRE 0 E 5: '))
comput= random.randint(0,5)
if num == 'comput':
    print('VOCÊ GANHOU! O numero sortedo foi {}'.format(comput))
else:
    print('VOCÊ PERDEU! O nùmero sorteado foi {}.'.format(comput))
