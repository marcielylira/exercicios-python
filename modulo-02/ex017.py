#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
oposto= float(input('Comprimento do cateto oposto: '))
adjacente= float(input('Comprimento do cateto adjacente: '))
hipotenusa= math.hypot(oposto,adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
