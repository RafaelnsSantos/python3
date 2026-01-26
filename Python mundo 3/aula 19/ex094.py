#crie um programa que leia nome,sexo e idade de varias pessoas,guardando os dados de cada 
# pessoa em um dicionario e todos os dicionarios em uma lista. no final mostre:
#A) quantas pessoas foram cadastradas
#B) a media de idade do grupo
#C) uma lista com todas as mulheres
#D) uma lista com todas as pessoas com idade acima da media

lista = []
media = 0 

while True:
    dados = {}
    dados['nome'] = str(input("Nome: ")).strip()
    dados['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]

    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input("Sexo invalido! digite o Sexo novamente [M/F]: ")).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break

    dados ['idade'] = int(input("Idade: "))
    media += dados['idade']
    lista.append(dados.copy())

    escolha_user = ' '
    while escolha_user != 'SN':
        escolha_user = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
        if escolha_user in 'SN':
            break

    if escolha_user == 'N':
        break

media = media/len(lista)
print("-=-"*15)
print(f"- O grupo tem {len(lista)} pessoas ")
print(f"- A media de idade do grupo e de {media:.2f} anos")
print("- Mulheres cadastradas foram:",end = '')

for p in lista: # para cada pessoa na lista ele vai verificar se o sexo dela e feminino
    if p['sexo'] == 'F':# se for ele vai printar o nome dela
        print(f" - {p['nome']}", end = ' ')
print()
print()
print("Lista de pessoas que estao acima da media: ")

for p in lista:
    if p['idade'] >= media:
        print(f" nome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']}; ")
        print()
