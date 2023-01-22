'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

maior = homem = mulher = 0

while True:
    age = int(input('Digite a idade: '))
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Masculino ou Feminino: ')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[32mDeseja continuar?\033[m ')).strip().upper()[0]
    if resp == 'N':
        break

    if age > 18:
        maior += 1
    if genero == 'M':
        homem += 1
    elif genero == 'F' and age < 20:
        mulher += 1

print(f'\n{maior} pessoas são maiores de 18 anos; \n{homem} homens foram cadastrados; \n{mulher} mulheres têm menos de 20 anos')