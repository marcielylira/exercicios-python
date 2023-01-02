#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.


from math import trunc
num= float(input('Digite um valor qualquer: '))
print('A porção inteira de {} é igual a {}'.format(num,trunc(num)))