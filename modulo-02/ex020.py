#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
nome1= str(input('primeiro nome: '))
nome2= str(input('segundo nome: '))
nome3= str(input('terceiro nome: '))
nome4= str(input('quarto nome: '))
lista= [nome1,nome2,nome3,nome4]
random.shuffle(lista)
print(lista)