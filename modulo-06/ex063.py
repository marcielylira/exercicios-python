''' Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8. '''

numero= int(input('Digite o termo que deseja encontrar: '))
termo_01= 0
termo_02= 1
contador= 3

while contador <= numero:
    termo_03= termo_01 + termo_02
    print('{} -> {}'.format(termo_01,termo_02), end= '')
    termo_01= termo_03
    termo_02= termo_01
    contador= contador + 1
print(' -> FIM')