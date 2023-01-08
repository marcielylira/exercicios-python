'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

a = float(input('Primeira medida: '))
b = float(input('Segunda medida: '))
c = float(input('Terceira medida: '))

if a == b and b == c:
    print('EQUILÁTERO')
elif a == b or a == c or b == c:
    print('ISÓSCELES')
elif a != b or a != c or b != c:
    print('ESCALENO')
