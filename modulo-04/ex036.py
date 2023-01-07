#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


casa= float(input('Valor da casa: '))
salario= float(input('Salário do comprador: '))
anos= int(input('Em quantos anos será financiado: '))

prestação= casa / (anos * 12)
print('Para financiar uma casa de R${:.2f}, o valor da prestação em {} anos será de R${:.2f}'.format(casa, anos,prestação))

if prestação > salario * 30 / 100:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')