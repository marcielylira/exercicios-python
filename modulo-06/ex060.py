'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

numero= int(input('Digite um número: '))
resultado= 1
contador= 1

while contador <= numero:
    resultado = resultado * contador
    contador = contador + 1
    print(resultado)



