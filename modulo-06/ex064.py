'''  Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). '''

número = 0
cont = 0
soma = 0

número = int(input('Digite um numero: '))

while número != 999:
    cont += 1
    soma += número
    número = int(input('Digite um numero: '))
print(''
      '')
print('\033[36mForam motrados {} numeros e a soma entre eles é igual a {}'.format(cont,soma))
print('FIM!!!')