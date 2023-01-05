#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano= int(input('Digite um ano para saber se ele é bissexto ou não: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('BISSEXTO')
else:
    print('NÃO É BISSEXTO')
