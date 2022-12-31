#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Informe sua quantia disponível: R$'))
dolar = real / 5.29
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(real,dolar))