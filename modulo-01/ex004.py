# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n1 = input('Escreva algo: ')
print('o tipo primitivo desse valor é ', type(n1))
print('só tem espaços? ', n1.isspace())
print('é um número? ', n1.isnumeric())
print('é alfabético? ', n1.isalpha())
print('é alfanumérico? ', n1.isalnum())
print('está em maiúsculas? ', n1.isupper())
print('esta é minúsculas? ', n1.islower())
print('está capitalizada? ', n1.istitle())