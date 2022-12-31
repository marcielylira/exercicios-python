#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro= float(input('Digite um valor em metro: '))
cm= metro * 100
mm= metro * 1000

print('{}m corresponde a {:.0f}cm e {:.0f}mm'.format(metro,cm,mm))