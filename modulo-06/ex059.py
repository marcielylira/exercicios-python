''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. '''

num_1= int(input('Digite o primeiro valor: '))
num_2= int(input('Digite o segundo valor: '))
escolha_usuario= 0
print(''
      '')
while escolha_usuario != 5:
    print('''\033[34m[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa\033[m''')
    print(''
          '')
    escolha_usuario= int(input('QUAL OPÇÃO VOCÊ ESCOLHE? '))
    if escolha_usuario == 1:
        soma= num_1 + num_2
        print('\033[32mA soma entre {} e {} é igual a {}\033[m'.format(num_1,num_2,soma))
    elif escolha_usuario == 2:
        multiplicação= num_1 * num_2
        print('\033[32mA multiplicação entre {} e {} é igual a {}.\033[m'.format(num_1,num_2,multiplicação))
    elif escolha_usuario == 3:
        if num_1 > num_2:
            maior= num_1
        else:
            maior= num_2
            print('\033[32mEntre {} e {}, o número maior é o {}\033[m'.format(num_1,num_2,maior))
    elif escolha_usuario == 4:
        print('Informe os números novamente.')
        num_1= int(input('Digite o primeiro valor: '))
        num_2= int(input('Digite o segundo valor: '))
    elif escolha_usuario == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print("=-="*10)
print('Fim do programa!')



