#Faça um programa que leia nome e peso de várias pessoas. guardando tudo em uma lista. No final. mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas Mais pesadas.
#C) Uma listagem com as pessoas mais leves.

dados = []
lista = []
cadastradas = 0
maior = 0
menor = 0
while True:
    nome = (input("Digite seu nome: "))
    peso = ( float(input("Digite seu peso: ")))
    cadastradas += 1

    if cadastradas == 1:
       maior = menor = peso
    else:
        if peso > maior:
            maior = peso

        elif peso < menor:
            menor = peso
            
#outra forma de pega o menor e o maior:
    #maior = max(p[1] for p in pessoas)
    #menor = min(p[1] for p in pessoas)

    lista.append([nome,peso])

    escolha_user = ' '
    while escolha_user !='SN':
        escolha_user = str(input("Quer continuar ? [S/N]")).strip().upper()[0]
        if escolha_user in'SN':
            break

    if escolha_user == 'N':
        break
print(f"Ao todo voce cadastrou {cadastradas} pessoas.")
print(f"o maior peso foi de {maior} kg o peso e de:",end = ' ')

# o p percorre a lista e se p[1] no caso aqui peso for igual a == maior peso declarados anterior mente: ele 
#vai printa na tela o p[0] que o nome da pessoa ou pessoas 
for p in lista:
    if p[1] == maior:
        print(f"{p[0]}",end = ' ')
print()

print(f"o menor peso foi de {menor}kg peso de:",end = ' ')

for p in lista:
    if p[1] == menor:
        print(f"{p[0]}",end = ' ')
