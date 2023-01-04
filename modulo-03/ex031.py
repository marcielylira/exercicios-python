#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km= float(input('Informe a distância da viagem em km: '))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print('Sua passagem sairá no valor de R${:.2f}'.format(preço))