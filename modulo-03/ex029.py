#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# multa vai custar R$7,00 por cada Km acima do limite.

km= float(input('Informe a velocidade que seu carro percorreu em km: '))
multa= (km - 80) * 7
if km > 80:
    print('Você foi multado em R${:.2f} por ultrapassar o limite de 80km/h.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
