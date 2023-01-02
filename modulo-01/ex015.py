#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km=float(input('Informe a quantidade de km: '))
dias=int(input('Informe a quantidade de dias: '))
preco= (km * 0.15) + (dias * 60)
print('Após ter percorrido {}km por {} dias, o aluguel do carro sairá no valor de R${:.2f}'.format(km,dias,preco))