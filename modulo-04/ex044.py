'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2% no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''


preçoProduto= float(input('Informe o preço do produto: R$'))
print('''
[1] - À vista dinheiro/cheque: 10% de desconto
[2] - À vista no cartão: 5% de desconto
[3] - Em até 2X no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros''')

formaPagamento= int(input('Informe a opção de pagamento: '))
print(''
      '')
if formaPagamento == 1:
    novoPreço= preçoProduto - (preçoProduto * 10 / 100)
    print('\033[34mA compra vai custar R${:.2f}'.format(novoPreço))
elif formaPagamento == 2:
    novoPreço= preçoProduto - (preçoProduto * 5 / 100)
    print('\033[34mA compra vai custar R${:.2f}'.format(novoPreço))
elif formaPagamento == 3:
    novoPreço= preçoProduto
    parcela= preçoProduto / 2
    print('\033[34mA compra será dividida em 2x de R${:.2f}.SEM JUROS'.format(parcela))
elif formaPagamento == 4:
    novoPreço= preçoProduto + (preçoProduto * 20 / 100)
    totalParc= int(input('Em quantas parcelas? '))
    parcela= novoPreço / totalParc
    print('\033[34mA compra será parcelada em {}x de R${:.2f}'.format(totalParc,parcela))
else:
    print('\033[31mOPÇÃO INVÁLIDA')