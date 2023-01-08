'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''


peso= float(input('Informe o peso(kg): '))
altura= float(input('Informe a altura(m): '))
print(""
      "")
imc= peso / (altura ** 2)
print('Seu IMC: \033[34m{:.1f}\033[m'.format(imc))

if imc < 18.5:
    print('\033[31mABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('\033[32mPESO IDEAL')
elif 25 <= imc < 30:
    print('\033[31mSOBREPESO')
elif 30 <= imc < 40:
    print('\033[31mOBESIDADE')
elif imc >= 40:
    print('\033[31mOBESIDADE MÓRBIDA')

