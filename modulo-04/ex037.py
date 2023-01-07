#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.

num= int(input('Digite um valor: '))
print('''Escolha uma base de conversão: 
1 - Converter para BINÁRIO
2 - Converter para OCTAL
3 - Converter para HEXADECIMAL''')
base= input('Sua escolha: ')

if base == '1':
    bin= bin(num)[2:]
    print(bin)
elif base == '2':
    oct= oct(num)[2:]
    print(oct)
elif base == '3':
    hxa= hex(num)[2:]
else:
    print('OPÇÃO INVÁLIDA!')