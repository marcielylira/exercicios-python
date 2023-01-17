'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo= primeiro
contador= 1
total= 0
mais= 10

while mais != 0:
    total= total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo= termo + razão
        contador = contador +1
    print('PAUSA')
    mais= int(input('Quantos termos você quer mais? '))
print(""
      "")
print('\033[34mProgressão finalizada com {} termos mostrados!'.format(total))