# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1= int(input('Primeiro número: '))
n2= int(input('Segundo número: '))

if n1 > n2:
    print('o \033[35mPRIMEIRO\033[m valor é o maior!')
elif n2 > n1:
    print('o \033[35mSEGUNDO\033[m valor é o maior!')
elif n1 == n2:
    print('\033[35mNÃO EXISTE MAIOR\033[m, os dois valores são iguais!')



