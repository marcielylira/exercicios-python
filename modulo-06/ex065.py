''' Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''


num= 1
soma= quantidade= media= 0
maior= menor= 0

print('mDigite quelquer número inteiro e quando desejar parar é só digitar 0'.upper())
print(''
      '')
while num != 0:
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor and num > 0:
            menor = num
media = soma / quantidade
print(''
      '')
print('A média de todos os valores lidos foi {:.2f}, sendo {} o número maior e {} o número menor'.format(media,maior,menor))
print('FIM')