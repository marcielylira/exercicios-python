#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num=int(input('Digite um número: '))
dobro= num * 2
triplo= num * 3
raizq= num**(1/2)
print('DOBRO: {}'.format(dobro))
print('TRIPLO: {}'.format(triplo))
print('RAIZ QUADRADA: {:.2f}'.format(raizq))

