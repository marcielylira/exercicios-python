#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a= int(input('Digite o número 1: '))
b= int(input('Digite o número 2: '))
c= int(input('Digite o número 3: '))

menor= a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
print('O menor número será {}'.format(menor))

maior= a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O maior número será {}'.format(maior))
