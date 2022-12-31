#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario= float(input('Informe o salário atual do funcionário: R$'))
novo= salario + (salario * 15 / 100)
print('O salario de R${:.2f}, com o aumento de 15% passará a valer R${:.2f}'.format(salario,novo))