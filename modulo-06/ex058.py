''' Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer. '''

import random
usuario= int(input('TENTE ADIVINHAR UM NÚMERO ENTRE 0 E 10: ' ))
computador= random.randint(0,10)
tentativas= 1
while usuario != computador:
    usuario= int(input('\033[31mNÚMERO ERRADO. Tente novamente: '))
    tentativas= tentativas + 1
else:
    print(""
          "")
    print('\033[34mPARABÉNS, VOCÊ ACERTOU!!!'.format(computador))
    print(""
          "")
    print('Você fez {} tentativas e o número escolhido foi {}.'.format(tentativas, computador))