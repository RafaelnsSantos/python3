#Crie um programa que vai ler varios numeros e colocar em uma lista. depois disso , crie duas lista extras
#que vao conter apenas os valores pares e os valores impares digitados respectivamente ao final mostre
#o conteudo das 3 listas geradas
lista = []
impar = []
par   = []

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    if valor%2 == 0:
        par.append(valor)
    elif valor%2 == 1:
        impar.append(valor)

    escolha_user = ' '
    while escolha_user != 'SN':
        escolha_user = str(input("Voce quer continuar? [S/N]: ")).strip().upper()
        if escolha_user in 'SN':
            break

    if escolha_user == 'N':
        break
print(f"Lista completa: {lista}")
print(f"A lista de par e: {par}")
print(f"A lista de impares e: {impar}")