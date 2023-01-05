#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

salario= float(input('Informe o salário atual: R$'))
if salario <= 1250:
    novo= salario + (salario * 15 / 100)
else:
    novo= salario + (salario * 10 / 100)
print('O salário com o reajuste sera de R${:.2f}'.format(novo))
