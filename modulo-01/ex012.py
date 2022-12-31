#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor= float(input('Informe o valor do produto: R$'))
novo= valor - (valor * 5 / 100)
print('O produto que estava custando R${}, com o desconto de 5% vai custar R${}'.format(valor,novo))





