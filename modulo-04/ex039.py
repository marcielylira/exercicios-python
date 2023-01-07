''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

atual= date.today().year
nasc= int(input('Digite o ano de nascimento: '))
idade= atual - nasc

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Já passou da sua hora de se alistar.')
    saldo= idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
elif idade < 18:
    print('Você é muito novo para se alistar.')
    saldo= 18 - idade
    print('Ainda faltam {} anos para você se alistar.'.format(saldo))