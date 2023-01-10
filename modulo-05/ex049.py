'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

print('\033[34m-----TABUADA-----\033[m')
m= 1
num= int(input('Digite um número: '))
print('\033[34m-\033[m'*17)
for c in range (1, 11):
    m = num * c
    print('\033[35m{} * {}\033[m = \033[37m{}\033[m'.format(num,c,m))