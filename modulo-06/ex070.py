'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

Gastos= Prod_Mil= 0
Menor_preço= cont= 0
Prod_Barato= ' '

while True:
    Nome_Pro= str(input('Produto: '))
    Preço_Prod= float(input('Preço: R$'))
    Gastos += Preço_Prod
    cont += 1

    if Preço_Prod > 1000:
        Prod_Mil += 1
    if cont == 1 or Preço_Prod < Menor_preço:
        Menor_preço = Preço_Prod
        Prod_Barato = Nome_Pro

    resp = ' '
    while resp not in 'SN':
        resp= str(input('Deseja continuar: ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de gastos foi de: R${Gastos:.2f}')
print(f'{Prod_Mil} produtos custaram mais de R$1.000')
print(f'O produto mais barato foi {Prod_Barato} e custa {Menor_preço:.2f}')
