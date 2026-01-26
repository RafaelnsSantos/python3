#Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o 
#programa devera perguntar perguntar se o usuario quer ou nao continuar no final mostre:
#A quantas pessoas tem mais de 18 anos , b) quantos homens foram cadastrados c)quantas mulheres, tem menos de 20 anos

maioridade = 0
homens = 0 
mulheres_menor_de_vinte = 0
while True:
    print('-=-'*7)
    print("|CADASTRO DE PESSOAS|")
    print("-=-"*7)
    idade = int(input("Digite sua idade: "))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
        if sexo not in 'MF':
            print("Sexo invalido")

    escolha_user = ' '
    while escolha_user not in 'SN':
        escolha_user = str(input("quer continuar [Sim/Nao]: ")).strip().upper()[0]
#certo:
    if idade > 18:
        maioridade += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres_menor_de_vinte += 1
#

    if escolha_user == 'N':
        break
print(f"total de pessoas com mais de 18 anos: {maioridade}\nao todo temos {homens} homens cadastrados \ne temos {mulheres_menor_de_vinte} mulheres com menos de 20 anos")