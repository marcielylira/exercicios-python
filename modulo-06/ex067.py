'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

num= 0

while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for c in range(1, 11):
        m = num * c
        print('{} * {} = {}'.format(num, c, m))
    print('-=-' * 10)
print('FIM DO PROGRAMA')



